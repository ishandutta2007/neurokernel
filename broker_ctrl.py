#!/usr/bin/env python

"""
Broker for routing between modules run in separate processes; data is
read from all modules before data is routed between modules.
Uses a separate port for control of modules.
"""

import logging, signal
import multiprocessing as mp
import numpy as np
import zmq
from zmq.eventloop.ioloop import IOLoop
from zmq.eventloop.zmqstream import ZMQStream

class Module(mp.Process):
    """
    Module to run in a process.

    Parameters
    ----------
    id : int
        Module ID.
    port_data : int
        Port to use when communicating with broker.
    port_ctrl : int
        Port used by broker to control module.
        
    Methods
    -------
    run()
        Body of process.
    process_data(data)
        Processes the specified data and returns a result for
        transmission to other modules.

    """

    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id')
        self.port_data = kwargs.pop('port_data')
        self.port_ctrl = kwargs.pop('port_ctrl')
        self.logger = logging.getLogger('module %s' % self.id)

        mp.Process.__init__(self, *args, **kwargs)
        
    def run(self):

        # Make the module processes ignore Ctrl-C:
        orig_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        
        # Connect to the broker:
        self.ctx = zmq.Context()
        self.sock_data = self.ctx.socket(zmq.DEALER)
        self.sock_data.setsockopt(zmq.IDENTITY, str(self.id))
        self.sock_data.connect("tcp://localhost:%i" % self.port_data)

        self.sock_ctrl = self.ctx.socket(zmq.DEALER)
        self.sock_ctrl.setsockopt(zmq.IDENTITY, str(self.id))
        self.sock_ctrl.connect("tcp://localhost:%i" % self.port_ctrl)

        # The modules send an initialization signal after connecting:
        self.sock_data.send('init')
       
        # Wait for data to arrive:
        self.ioloop = IOLoop.instance()
        self.stream_data = ZMQStream(self.sock_data, self.ioloop)
        self.stream_ctrl = ZMQStream(self.sock_ctrl, self.ioloop)

        def handler(msg):
            data = msg[0].decode()
            if data == 'quit':
                self.stream_data.flush()                
                self.stream_ctrl.flush()
                self.ioloop.stop()
        self.stream_ctrl.on_recv(handler)
        
        def handler(msg):
            data = msg[0].decode()
            self.logger.info('received: %s' % data)
            result = self.process_data(data)
            self.sock_data.send(result)
        self.stream_data.on_recv(handler)

        self.ioloop.start()
        
        # Restore SIGINT signal handler before exiting:
        signal.signal(signal.SIGINT, orig_handler)
        self.logger.info('done')
        
    def process_data(self, data):
        """
        This method should be implemented to do something with its
        arguments and produce output.
        """

        return ''
    
class ModuleBroker(object):
    """
    Broker for communicating between modules.

    Parameters
    ----------
    port_data : int
        Port to use for communication with modules.
    port_ctrl : int
        Port used to control modules.
        
    Methods
    -------
    create(module_class)
        Create an instance of the specified module class and connect
        it to the broker.
    run()
        Body of broker.
    process_data(in_data)
        Process data from modules; the output should be in a format
        that can be transmitted to the modules by the `send_all()`
        method.
    
    """
    
    def __init__(self, port_data=5000, port_ctrl=5001):

        self.logger = logging.getLogger('broker  ')
        self.port_data = port_data
        self.port_ctrl = port_ctrl

        # Set up a router socket to communicate with the started
        # processes:
        self.ctx = zmq.Context()
        self.sock_data = self.ctx.socket(zmq.ROUTER)
        self.sock_data.bind("tcp://*:%i" % self.port_data)

        self.sock_ctrl = self.ctx.socket(zmq.ROUTER)
        self.sock_ctrl.bind("tcp://*:%i" % self.port_ctrl)
        
        # Dictionary for mapping module IDs to module instances:
        self.id_to_mod_dict = {}

        # Dictionary for mapping module instances to module IDs:
        self.mod_to_id_dict = {}

    @property
    def N(self):
        """
        Number of module instances.
        """
        
        return len(self.id_to_mod_dict)
    
    def create(self, module_class):
        """
        Create instance of module to the network managed by the broker.
        """

        if not issubclass(module_class, Module):
            raise ValueError('subclass of Module class must be specified')
        m = module_class(id=self.N, port_data=self.port_data, port_ctrl=self.port_ctrl)
        m.start()
        self.id_to_mod_dict[str(self.N)] = m
        self.mod_to_id_dict[m] = str(self.N)
                    
    def run(self):
        """
        Body of broker.
        """

        self.ioloop = IOLoop.instance()
        self.stream = ZMQStream(self.sock_data, self.ioloop)
        def handler(msg):
            try:
                # Need to cast the message contents to non-Unicode
                # strings for some reason:
                addr = str(msg[0].decode())
                data = str(msg[1].decode())
                self.logger.info('received from %s: %s' % (addr, data))
                if addr in handler.ack_list:
                    handler.ack_list.remove(addr)
                handler.in_data.append((addr, data))
                if len(handler.ack_list) == 0:
                    self.logger.info('barrier reached')
                    out_data = self.process_data(handler.in_data)          
                    for entry in out_data:
                        self.logger.info('sent to %s: %s' % entry)
                        self.sock_data.send_multipart(entry)
                            
                    # Reset variables:
                    handler.ack_list = self.id_to_mod_dict.keys()
                    handler.in_data = []        
            except KeyboardInterrupt:
                self.stream.flush()
                self.ioloop.stop()
                            
        handler.ack_list = self.id_to_mod_dict.keys()
        handler.in_data = []
        self.stream.on_recv(handler)
        try:
            self.ioloop.start()
        except KeyboardInterrupt:
            self.ioloop.stop()
            
        # Tell the modules to terminate:
        for i in self.id_to_mod_dict.keys():
            entry = (str(i), 'quit')
            self.logger.info('sent to %s: %s' % entry)
            self.sock_ctrl.send_multipart(entry)
        self.logger.info('done')
        
    def process_data(self, in_data):
        """
        Figure out how to route data entries in the specified
        list. Each entry is a tuple containing the ID of the source
        module and the data itself.
        """

        return in_data
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s')
    b = ModuleBroker()
    b.create(Module)
    b.create(Module)
    b.create(Module)

    b.run()