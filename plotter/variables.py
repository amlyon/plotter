import numpy as np

class Variable(object):
    def __init__(self, var, bins, xlabel, ylabel, label=None, extra_label=None, extra_selection=None):
        self.var = var
        self.bins = bins
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.extra_label = extra_label
        self.extra_selection = extra_selection
        self.label = self.var if label is None else self.label
        if self.extra_label is not None:
            self.label = '_'.join([self.label, self.extra_label])
    
    
m12_bins_displaced_1 = np.linspace(0., 10., 10 + 1)    
m12_bins_displaced_2 = np.array([0., 1., 2., 3., 4., 5., 10]) 
m12_bins_displaced_3 = np.array([0., 1., 2., 3., 10])     
    
# variables
variables = [
    Variable('l0_pt', np.linspace(0.,100.,20 + 1), 'l_{1} p_{T} (GeV)', 'events'),
    Variable('l1_pt', np.linspace(0., 50.,20 + 1), 'l_{2} p_{T} (GeV)', 'events'),
    Variable('l2_pt', np.linspace(0., 30.,20 + 1), 'l_{3} p_{T} (GeV)', 'events'),

    Variable('l0_pt', np.linspace(0.,100.,20 + 1), 'l_{1} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp<=0.5'                  , extra_label='l0_pt_lt_0p5'    ),
    Variable('l0_pt', np.linspace(0.,100.,20 + 1), 'l_{1} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>0.5 & hnl_2d_disp<=2.0', extra_label='l0_pt_0p5_to_2p0'),
    Variable('l0_pt', np.linspace(0.,100.,10 + 1), 'l_{1} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0'                   , extra_label='l0_pt_mt_2p0'    ),

    Variable('l1_pt', np.linspace(0., 50.,20 + 1), 'l_{2} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp<=0.5'                  , extra_label='l1_pt_lt_0p5'    ),
    Variable('l1_pt', np.linspace(0., 50.,20 + 1), 'l_{2} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>0.5 & hnl_2d_disp<=2.0', extra_label='l1_pt_0p5_to_2p0'),
    Variable('l1_pt', np.linspace(0., 50.,10 + 1), 'l_{2} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0'                   , extra_label='l1_pt_mt_2p0'    ),

    Variable('l2_pt', np.linspace(0., 30.,20 + 1), 'l_{3} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp<=0.5'                  , extra_label='l2_pt_lt_0p5'    ),
    Variable('l2_pt', np.linspace(0., 30.,20 + 1), 'l_{3} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>0.5 & hnl_2d_disp<=2.0', extra_label='l2_pt_0p5_to_2p0'),
    Variable('l2_pt', np.linspace(0., 30.,10 + 1), 'l_{3} p_{T} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0'                   , extra_label='l2_pt_mt_2p0'    ),

    Variable('hnl_m_12', m12_bins_displaced_1, 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp<=0.5'                  , extra_label='lxy_lt_0p5'    ),
    Variable('hnl_m_12', m12_bins_displaced_2, 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>0.5 & hnl_2d_disp<=2.0', extra_label='lxy_0p5_to_2p0'),
    Variable('hnl_m_12', m12_bins_displaced_3, 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0'                   , extra_label='lxy_mt_2p0'    ),

#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp<=0.5'                  , extra_label='lxy_lt_0p5'    ),
#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>0.5 & hnl_2d_disp<=2.0', extra_label='lxy_0p5_to_2p0'),
#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0'                   , extra_label='lxy_mt_2p0'    ),

#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp<=2.0'                  , extra_label='lxy_lt_2p0'    ),
#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>2.0 & hnl_2d_disp<=5.0', extra_label='lxy_0p5_to_2p0'),
#     Variable('hnl_m_12', np.linspace(0., 12., 12 + 1), 'm_{23} (GeV)', 'events', extra_selection='hnl_2d_disp>5.0'                   , extra_label='lxy_mt_5p0'    ),

    Variable('hnl_2d_disp'    , np.linspace( 0, 30, 25 + 1) , 'L_{xy} (cm)'       , 'events'),
    Variable('hnl_2d_disp_sig', np.linspace( 0,200, 25 + 1) , 'L_{xy}/\sigma_{xy}', 'events'),
    Variable('nbj'            , np.linspace( 0,  5,  5 + 1) , '#b-jet'            , 'events'),
    Variable('hnl_w_vis_m'    , np.linspace( 0,150, 40 + 1) , 'm_{3l}'         , 'events'),
    Variable('hnl_q_01'       , np.linspace(-3,  3,  3 + 1) , 'q_{12}'            , 'events'),
    Variable('sv_cos'         , np.linspace( 0,  1, 30 + 1) , '\cos\alpha'        , 'events'),
    Variable('sv_prob'        , np.linspace( 0,  1, 30 + 1) , 'SV probability'    , 'events'),
]

