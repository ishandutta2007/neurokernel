# use of 0.0 instead of 0 where float is expected

MED_INPUTS = ['L1', 'L2', 'L3', 'L4', 'L5']
NEURON_LIST = [
    {'name':'L1', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'L2', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'L3', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'L4', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},
    {'name':'L5', 'model':'port_in_gpot', 'columnar':True, 'output':False,
     'extern':False, 'input':True, 'spiking':False},

    #
    {'name':'C2', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-5.0, 'V2':25.0, 'V3':20.0, 'V4':35.0,
    'V_l':-60.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':2.0, 'G_k':16.0,
    'phi':0.001, 'initV':-53.51, 'initn':0.0104, 'offset':0.0},
    {'name':'C3', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-5.0, 'V2':25.0, 'V3':20.0, 'V4':35.0,
    'V_l':-60.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':2.0, 'G_k':16.0,
    'phi':0.001, 'initV':-53.1, 'initn':0.0104, 'offset':0.0},
    {'name':'Mi1', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-50.8, 'initn':0.3525, 'offset':0.0},
    {'name':'Tm1', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-46.07, 'initn':0.3525, 'offset':0.0},
    {'name':'Tm2', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.11, 'initn':0.3525, 'offset':0.0},
    {'name':'Mi4', 'model':'MorrisLecar_a', 'columnar':True, 'output':False,
    'extern':False, 'public':False, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-46.11, 'initn':0.3525, 'offset':0.0},
    {'name':'Mi9', 'model':'MorrisLecar_a', 'columnar':True, 'output':False,
    'extern':False, 'public':False, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.26, 'initn':0.3525, 'offset':0.0},
    {'name':'Tm9', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.79, 'initn':0.3525, 'offset':0.0},
    {'name':'Tm20', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-46.01, 'initn':0.3525, 'offset':0.0},
    {'name':'Tm3', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-47.504, 'initn':0.3525, 'offset':0.0},
    {'name':'T4a', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.9, 'initn':0.3525, 'offset':0.0},
    {'name':'T4b', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.9, 'initn':0.3525, 'offset':0.0},
    {'name':'T4c', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.9, 'initn':0.3525, 'offset':0.0},
    {'name':'T4d', 'model':'MorrisLecar_a', 'columnar':True, 'output':True,
    'extern':False, 'public':True, 'spiking':False,
    'V1':-20.0, 'V2':50.0, 'V3':-40.0, 'V4':20.0,
    'V_l':-40.0, 'V_ca':120.0, 'V_k':-80.0,
    'G_l':3.0, 'G_ca':4.0, 'G_k':16.0,
    'phi':0.001, 'initV':-45.9, 'initn':0.3525, 'offset':0.0}
]

# use of 0.0 instead of 0 where float is expected
SYNAPSE_LIST = [
    {'prename':'L1', 'postname':'Mi1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-46.0, 'slope':0.03, 'power':1.0, 'saturation':10.0,
    'scale':127, 'mode':0},
    {'prename':'L2', 'postname':'Tm1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':153, 'mode':0},
    {'prename':'L2', 'postname':'Tm2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':106, 'mode':0},
    {'prename':'L2', 'postname':'Tm20', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':9, 'mode':0},
    {'prename':'L3', 'postname':'C3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':9, 'mode':0},
    {'prename':'L3', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':30, 'mode':0},
    {'prename':'L3', 'postname':'Tm20', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':20, 'mode':0},
    {'prename':'L3', 'postname':'Tm9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.02, 'power':1.0, 'saturation':10.0,
    'scale':17, 'mode':0},
    {'prename':'L4', 'postname':'Tm2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-60.5, 'slope':0.02, 'power':1.0, 'saturation':5.0,
    'scale':5, 'mode':0},
    {'prename':'L5', 'postname':'C2', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-58.5, 'slope':0.02, 'power':1.0, 'saturation':5.0,
    'scale':5, 'mode':0},
    {'prename':'L5', 'postname':'C3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-58.5, 'slope':0.02, 'power':1.0, 'saturation':5.0,
    'scale':5, 'mode':0},
    {'prename':'L5', 'postname':'Mi1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-58.5, 'slope':0.03, 'power':1.0, 'saturation':5.0,
    'scale':33, 'mode':0},
    {'prename':'L5', 'postname':'Mi4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-58.5, 'slope':0.02, 'power':1.0, 'saturation':5.0,
    'scale':10, 'mode':0},
    {'prename':'C2', 'postname':'Mi1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':22, 'mode':0},
    {'prename':'C2', 'postname':'Tm1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-54.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':8, 'mode':0},
    {'prename':'C3', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':7, 'mode':0},
    {'prename':'C3', 'postname':'Tm1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':18, 'mode':0},
    {'prename':'C3', 'postname':'Tm20', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':10, 'mode':0},
    {'prename':'C3', 'postname':'Tm9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-53.9, 'slope':0.04, 'power':1.0, 'saturation':3.0,
    'scale':3, 'mode':0},
    {'prename':'Mi1', 'postname':'Mi4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':5, 'mode':0},
    {'prename':'Mi1', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':2, 'mode':0},
    {'prename':'Tm1', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':4, 'mode':0},
    {'prename':'Tm2', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0},
    {'prename':'Tm2', 'postname':'C3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':4, 'mode':0},
    {'prename':'Mi4', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':19, 'mode':0},
    {'prename':'Mi4', 'postname':'Tm20', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':9, 'mode':0},
    {'prename':'Mi4', 'postname':'Tm9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':9, 'mode':0},
    {'prename':'Mi9', 'postname':'Mi4', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':5, 'mode':0},
    {'prename':'Mi9', 'postname':'Tm1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':5, 'mode':0},
    {'prename':'Tm20', 'postname':'Mi9', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':5, 'mode':0},
    {'prename':'L1', 'postname':'Tm3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':30, 'mode':0},
    {'prename':'L5', 'postname':'Tm3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-80.0, 'delay':1,
    'threshold':-58.5, 'slope':0.04, 'power':1.0, 'saturation':5.0,
    'scale':8, 'mode':0},
    {'prename':'Mi1', 'postname':'Tm3', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':9, 'mode':0},
    {'prename':'Mi1', 'postname':'T4a', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':31, 'mode':0},
    {'prename':'Mi1', 'postname':'T4b', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':31, 'mode':0},
    {'prename':'Mi1', 'postname':'T4c', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':31, 'mode':0},
    {'prename':'Mi1', 'postname':'T4d', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':31, 'mode':0},
    {'prename':'Mi1', 'postname':'L1', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':8, 'mode':0},
    {'prename':'Mi1', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-46.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':8, 'mode':0},
    {'prename':'Tm1', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':13, 'mode':0},
    {'prename':'Tm2', 'postname':'L5', 'model':'power_gpot_gpot_sig',
    'cart':None, 'reverse':-10.0, 'delay':1,
    'threshold':-40.0, 'slope':0.04, 'power':1.0, 'saturation':10.0,
    'scale':13, 'mode':0},
    {'prename':'Tm3', 'postname':'T4a', 'model':'power_gpot_gpot_sig',
    'cart':1, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':10, 'mode':0},
    {'prename':'Tm3', 'postname':'T4a', 'model':'power_gpot_gpot_sig',
    'cart':2, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'Tm3', 'postname':'T4a', 'model':'power_gpot_gpot_sig',
    'cart':6, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'Tm3', 'postname':'T4b', 'model':'power_gpot_gpot_sig',
    'cart':4, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':10, 'mode':0},
    {'prename':'Tm3', 'postname':'T4b', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'Tm3', 'postname':'T4b', 'model':'power_gpot_gpot_sig',
    'cart':5, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':3, 'mode':0},
    {'prename':'Tm3', 'postname':'T4c', 'model':'power_gpot_gpot_sig',
    'cart':5, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0},
    {'prename':'Tm3', 'postname':'T4c', 'model':'power_gpot_gpot_sig',
    'cart':6, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0},
    {'prename':'Tm3', 'postname':'T4d', 'model':'power_gpot_gpot_sig',
    'cart':2, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0},
    {'prename':'Tm3', 'postname':'T4d', 'model':'power_gpot_gpot_sig',
    'cart':3, 'reverse':-80.0, 'delay':4,
    'threshold':-40.0, 'slope':0.06, 'power':1.0, 'saturation':10.0,
    'scale':7, 'mode':0}
]