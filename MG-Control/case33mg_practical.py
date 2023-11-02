from numpy import array

def case33mg():
    ppc = {"version": '2'}
    ppc["baseMVA"] = 100.0


    pi = 3.141592653589793
    ppc["baseOmega"] = 2 * pi * 50
    ppc["refbus"] = 15  # set as the first bus. reference bus for voltage angle; angle of refbus is set as 0.

    ## bus data
    # bus_i type Pd(p_set_point) Qd(q_set_point) Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([ 
        [	2,	1,	0.1  , 0.06 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	3,	1,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	4,	1,	0.12 , 0.08 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	5,	1,	0.06 , 0.03 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	6,	1,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	7,	1,	0.2  , 0.1  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	8,	1,	0.2  , 0.1  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	9,	1,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	10,	3,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	11,	1,	0.045, 0.03 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	12,	1,	0.06 , 0.035,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	13,	1,	0.06 , 0.035,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	14,	1,	0.12 , 0.08 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	15,	2,	0.06 , 0.01 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	16,	1,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	17,	1,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	18,	1,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	19,	1,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	20,	1,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	21,	2,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	22,	1,	0.09 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	23,	2,	0.09 , 0.05 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	24,	1,	0.42 , 0.2  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	25,	1,	0.42 , 0.2  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	26,	1,	0.06 , 0.025,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	27,	1,	0.06 , 0.025,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	28,	2,	0.06 , 0.02 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	29,	1,	0.12 , 0.07 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	30,	2,	0.2  , 0.6  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	31,	1,	0.15 , 0.07 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	32,	1,	0.21 , 0.1  ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9],
        [	33,	1,	0.06 , 0.04 ,	0,	0,	1,	1,	0,	12.66,	1,	1.1,	0.9]
    ])
 
    ## converter data
    # conv bus, r_c(Om), L_c(H), r_f(Om), L_f(mH), C_f(F), omega_c(rad/s), K_p,    K_q,   K_pv, K_iv, K_pc, K_ic, F,   P_set,    Q_set, E_set
    ppc["gen"] = array([
        [15,    0.03, 0.35e-3,  0.1,     1.35e-3, 50e-6, 31.41,    1.1* 0.08 * 9.4e-5,   0.09 * 1.3e-3, 0.05, 390, 10.5, 16e3, 0.75, 810000,   2500000 ,  12913.2 ],
        [21,    0.03, 0.35e-3,  0.1,     1.35e-3, 50e-6, 31.41,    1.1* 0.04 * 9.4e-5,   0.09 * 1.3e-3, 0.05, 390, 10.5, 16e3, 0.75, 2000000,  2500000,   12913.1 ],
        [28,    0.03, 0.35e-3,  0.1,     1.35e-3, 50e-6, 31.41,    1.1* 0.01 * 9.4e-5,   0.09 * 1.3e-3, 0.05, 390, 10.5, 16e3, 0.75, 1000000,  2500000,   12660.0]
    ]) 
    
    ## load data
    # constant impedance load
    # load bus, r_L(Om), x_L(Om)
    ppc["load_z"] = array([
        [2,  1170.79,     702.47  ],
        [3,  1475.58,     655.81  ],
        [4,  918.77 ,     612.51  ],
        [5,  2128.05,     1064.02 ],
        [6,  2406.63,     802.21  ],
        [7,  641.11 ,     320.55  ],
        [8,  642.5  ,     321.25  ],
        [9,  2424.77,     808.26  ],
        [10, 2442.75,     814.25  ],
        [11, 2503.93,     1669.29 ],
        [12, 2022.17,     1179.6  ],
        [13, 2014.8 ,     1175.3  ],
        [15, 2625.12,     437.52  ],
        [16, 2422.21,     807.4   ],
        [17, 2413.3 ,     804.43  ],
        [19, 1478.85,     657.27  ],
        [21, 1502.0 ,     667.56  ],
        [22, 1500.12,     666.72  ],
        [23, 1347.26,     748.48  ],
        [24, 303.92 ,     144.72  ],
        [25, 301.91 ,     143.77  ],
        [27, 2287.69,     953.2   ],
        [28, 2442.75,     814.25  ],
        [29, 1007.31,     587.6   ],
        [30, 80.94  ,     242.82  ],
        [31, 879.5  ,     410.44  ],
        [32, 622.57 ,     296.46  ],
        [33, 1849.66,     1233.1  ]
    ]) 
    
    # induction motor load
    # load buses, L_Ms, L_Mm, L_Mr, r_Mr, r_Ms, H_M, a_M, b_M, c_M, T_M^0
    ppc["load_im"] = array([  
        [20,      10*  0.0015,  10*  0.043, 10* 0.002,   0.1,  0.22,     2000* 1.2,  2, 0.08,  -1,   286.47889757  ], 
        [26,      10*  0.0015,  10*  0.043, 10* 0.002,   0.1,  0.22,     4000* 1.2,  2, 0.08,  -1,   190.98593171  ]
    ])
    
    # variable frequency drive load
    # load buses, r_A,  L_A, L_DC, C_DC, i_max, K_max, T_max, K_DP, w_Dref, alpha,| L_Ms, L_Mm, L_Mr, r_Mr, r_Ms, H_M, a_M, b_M, c_M, T_M^0
    ppc["load_vfd"] = array([
        [14,  0.0001, 0.002, 0.0005, 1e-5, 50, 4, 600, 10, 2*pi*50, 1, 10*  0.0015,  10*  0.043, 10* 0.002,   0.1,  0.22,     2000* 1.2,  2, 0.08,  -1,   381.97186342  ],  
        [18,  0.0001, 0.002, 0.0005, 1e-5, 50, 4, 600, 10, 2*pi*50, 1, 10*  0.0015,  10*  0.043, 10* 0.002,   0.1,  0.22,     5000* 1.2,  2, 0.08,  -1,   286.47889757  ] 
    ])
    
    ## branch data
    # fbus, tbus, r_B, x_B
    ppc["branch"] = array([
        [2,     3,	0.493,  0.2511  , 1],
        [3,     4,	0.366,  0.1864  , 1],
        [4,     5,	0.3811, 0.1941  , 1],
        [5,     6,	0.819,  0.707   , 1],
        [6,     7,	0.1872, 0.6188  , 1],
        [7,     8,	0.7114, 0.2351  , 1],
        [8,     9,	1.03,   0.74    , 1],
        [9,     10,	1.044,  0.74    , 1],
        [10,    11,	0.1966, 0.065   , 1],
        [11,    12,	0.3744, 0.1238  , 1],
        [12,    13,	1.468,  1.155   , 1],
        [13,	14,	0.5416, 0.7129  , 1],
        [14,	15,	0.591,  0.526   , 1],
        [15,	16,	0.7463, 0.545   , 1],
        [16,	17,	1.289,  1.721   , 1],
        [17,	18,	0.732,  0.574   , 1],
        [2,	    19,	0.164,  0.1565  , 1],
        [19,    20,	1.5042, 1.3554  , 1],
        [20,    21,	0.4095, 0.4784  , 1],
        [21,    22,	0.7089, 0.9373  , 1],
        [3,	    23,	0.4512, 0.3083  , 1],
        [23,    24,	0.898,  0.7091  , 1],
        [24,    25,	0.896,  0.7011  , 1],
        [6,	    26,	0.203,  0.1034  , 1],
        [26,    27,	0.2842, 0.1447  , 1],
        [27,    28,	1.059,  0.9337  , 1],
        [28,    29,	0.8042, 0.7006  , 1],
        [29,    30,	0.5075, 0.2585  , 1],
        [30,    31,	0.9744, 0.963   , 1],
        [31,    32,	0.3105, 0.3619  , 1],
        [32,    33,	0.341,  0.5302  , 1],
        [18,	22,	1e8,    1e8     , 0]
    ])

    ppc['xz_guess'] = array([ 4.72868190e-02,  1.09750370e-02,  8.05270075e+05,  2.00000000e+06,  1.00000000e+06,  8.19131695e+05,  1.41901701e+05,  1.41451151e+06,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        6.23602263e+01,  1.55226586e+02,  8.02104091e+01, -6.34336721e+01, -3.65553730e+00, -1.10857149e+02,  1.00000000e-02,  1.00000000e-02,  1.00000000e-02,  1.00000000e-02,  1.29132000e+04,  1.28987655e+04,  1.26592376e+04,  0.00000000e+00,  6.10396613e+02,  1.38941179e+02,  6.23602263e+01,  1.55226586e+02,  8.02104091e+01, -6.34336721e+01,
       -3.65553730e+00, -1.10857149e+02,  8.03890476e+00,  7.22990434e+00,  9.68118754e+00,  4.81845644e+00,  4.78674177e+00,  1.59698210e+01,  1.59517826e+01,  4.75798843e+00,  4.73717798e+00,  3.55673972e+00,  4.73199515e+00,  4.68873541e+00,  4.64640833e+00,  4.65150460e+00,  4.65813794e+00,  7.19918337e+00,  7.10824310e+00,  7.11163665e+00,
        7.27262792e+00,  3.40817560e+01,  3.41846650e+01,  4.78506339e+00,  4.75638885e+00,  9.61887123e+00,  1.66307506e+01,  1.20960263e+01,  1.69483815e+01,  4.85445192e+00, -4.53987730e+00, -3.01103316e+00, -6.15593395e+00, -2.29273897e+00, -1.51880197e+00, -7.72621661e+00, -7.75497507e+00, -1.54136652e+00, -1.54800532e+00, -2.34377422e+00,
       -2.73346776e+00, -2.72730215e+00, -7.74401388e-01, -1.55219769e+00, -1.56005117e+00, -2.96151594e+00, -2.76469501e+00, -2.76876659e+00, -3.82350512e+00, -1.53371625e+01, -1.54141687e+01, -1.91990274e+00, -1.52767034e+00, -5.45533998e+00, -4.76949286e+01, -5.46207074e+00, -7.81992468e+00, -3.15274275e+00,  1.28590430e+04,  1.28676658e+04,
        1.28419216e+04,  1.25974564e+04,  1.15645608e+01, -1.99744622e+01,  5.42169994e+02,  1.75967222e+02,  9.33754167e+00,  6.98943323e+00,  7.12709638e+00,  4.78965251e+00, -6.21290524e+00, -3.11941658e+00, -2.81390148e+00, -1.91762347e+00,  1.18641526e+02,  3.58725737e+01,  2.61913865e+01,  2.13729311e+01,  2.23170180e+01,  6.34719864e+00,
       -9.60457808e+00, -1.43625615e+01, -1.90997385e+01, -2.26564775e+01, -2.73884689e+01, -3.20772013e+01, -4.14147422e+01,  1.62990758e+01,  1.16475712e+01,  6.98943323e+00, -1.26680431e+02, -1.33879613e+02, -1.41006707e+02,  7.11163665e+00,  7.55390489e+01,  6.82664209e+01,  3.41846650e+01, -5.73082614e+00, -1.05204781e+01, -1.53055400e+01,
        6.01484816e+01,  5.05296104e+01,  3.38988598e+01,  2.18028334e+01,  4.85445192e+00, -1.01252330e+04,  1.21932193e+01,  4.97790884e+01,  5.59350220e+01,  5.82277602e+01,  2.38396149e+01,  3.15658348e+01,  3.93208066e+01,  4.08621696e+01,  4.24101726e+01,  4.47539454e+01,  4.74874080e+01,  5.02147041e+01,  5.64276053e+01, -6.23166543e+00,
       -4.67946775e+00, -3.11941658e+00, -7.65334191e+00, -4.69182608e+00, -1.87792432e+00, -2.76876659e+00, -3.45748363e+01, -3.07513312e+01, -1.54141688e+01,  3.59069445e+01,  3.78245681e+01,  3.97444718e+01, -6.95850068e+01, -6.41296668e+01, -1.64347382e+01, -1.09726674e+01, -3.15274275e+00, -9.39327503e+03,  1.26273213e+04,  1.25718928e+04,
        1.25680423e+04,  1.25689177e+04,  1.25925803e+04,  1.26031545e+04,  1.26060602e+04,  1.26450504e+04,  1.26902829e+04,  1.26967945e+04,  1.27108177e+04,  1.28058719e+04,  1.28590430e+04,  1.29132000e+04,  1.28976397e+04,  1.28745727e+04,  1.28676658e+04,  1.26468992e+04,  1.28419216e+04,  1.28987655e+04,  1.28911288e+04,  1.25271502e+04,
        1.24440411e+04,  1.24026048e+04,  1.25974564e+04,  1.26059196e+04,  1.26592376e+04,  1.25621149e+04,  1.25198936e+04,  1.24710359e+04,  1.24602951e+04,  1.24569681e+04,  3.32571486e+02,  2.96769341e+02,  2.71863547e+02,  2.45462962e+02,  1.82663764e+02,  1.64391217e+02,  1.40443056e+02,  1.07050013e+02,  7.50182032e+01,  6.79218463e+01,
        5.39708409e+01,  1.58930080e+01,  1.15645608e+01,  0.00000000e+00, -4.23230436e+00, -1.82459404e+01, -1.99744622e+01,  3.53652122e+02,  5.42169994e+02,  6.10396613e+02,  6.05693655e+02,  2.89080818e+02,  2.68287795e+02,  2.58132021e+02,  1.75967222e+02,  1.66739792e+02,  1.38941179e+02,  1.52761416e+02,  1.72245317e+02,  1.55614724e+02,
        1.51131292e+02,  1.49632546e+02])

    return ppc

 












































