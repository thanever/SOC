# Copyright (c) 1996-2015 PSERC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Power flow data for 9 bus, 3 generator case.
    Modifications:
    1. Add 3 new lines to complicate the network
    2. twice the loads
    Additional data:
    1. Add 3 columns for gen data 
"""

from numpy import array

def case9():
    """Power flow data for 9 bus, 3 generator case.
    Please see L{caseformat} for details on the case file format.

    Based on data from Joe H. Chow's book, p. 70.

    @return: Power flow data for 9 bus, 3 generator case.
    """
    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base
    ppc["baseMVA"] = 100.0

    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    #! ratio_ls_max - maximal ratio of load shedding
    #! w_d - load shedding cost, the unit is $/MW
    ppc["bus"] = array([
        [1, 3, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [2, 2, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [3, 2, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [4, 1, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [5, 1, 90,    30,   0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [6, 1, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [7, 1, 100,   35,   0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 8],
        [8, 1, 0,     0,    0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 10],
        [9, 1, 125,   50,   0, 0, 1, 1, 0, 345, 1, 1.1, 0.9, 0.8, 6]
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    #! gen_type  - 0 for conventional generators and 1 for VRE-based generators
    #! phi_v_min - minimal power factor of inverters
    #! s_v_max   - MVA rating of inverters
    #! r_+2      - upward ramp rate for the second stage
    #! r_-2      - downward ramp rate for the second stage, r_-2  = r_+2 if the generator does not participate into regulation 
    #! r_+3      - upward ramp rate for the second stage
    #! r_-3      - downward ramp rate for the second stage, r_-2  = r_+2 if the generator does not participate into regulation 
    ppc["gen"] = array([
        [1, 0,   0, 300, -300, 1, 100, 1, 250, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.95, 250*1.5, 20, 40, 30, 60],
        [2, 163, 0, 300, -300, 1, 100, 1, 300, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.95, 300*1.5, 20, 40, 30, 60],
        [3, 85,  0, 300, -300, 1, 100, 1, 270, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.95, 270*1.5, 0,  0,  30, 60]
    ])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    #! w_s - cost of line switching in the third-stage corrective control
    ppc["branch"] = array([
        [1, 4, 0,      0.0576, 0,     250*3, 250, 250, 1, 0, 1, -30, 30, 0.1],
        [4, 5, 0.017,  0.092,  0.158, 250, 250, 250, 0, 0, 1, -30, 30, 0.1],
        [5, 6, 0.039,  0.17,   0.358, 150, 150, 150, 0, 0, 1, -30, 30, 0.1],
        [3, 6, 0,      0.0586, 0,     300*3, 300, 300, 1, 0, 1, -30, 30, 0.1],
        [6, 7, 0.0119, 0.1008, 0.209, 150, 150, 150, 0, 0, 1, -30, 30, 0.1],
        [7, 8, 0.0085, 0.072,  0.149, 250, 250, 250, 0, 0, 1, -30, 30, 0.1],
        [8, 2, 0,      0.0625, 0,     250*3, 250, 250, 1, 0, 1, -30, 30, 0.1],
        [8, 9, 0.032,  0.161,  0.306, 250, 250, 250, 0, 0, 1, -30, 30, 0.1],
        [9, 4, 0.01,   0.085,  0.176, 250, 250, 250, 0, 0, 1, -30, 30, 0.1],
        [5, 7, 0.002,  0.02,   0.04  ,50,  50,  50,  0, 0, 1, -30, 30, 0.1],
        [5, 9, 0.002,  0.02,   0.04  ,50,  50,  50,  0, 0, 1, -30, 30, 0.1],
        [7, 9, 0.002,  0.02,   0.04  ,50,  50,  50,  0, 0, 1, -30, 30, 0.1],
        [4, 6, 0.02,   0.2,    0.4  , 300, 300, 300, 0, 0, 1, -30, 30, 0.1],
        [4, 8, 0.02,   0.2,    0.4  , 300, 300, 300, 0, 0, 1, -30, 30, 0.1] 
    ])

    ##-----  OPF Data  -----##
    ## area data
    # area refbus
    ppc["areas"] = array([
        [1, 5]
    ])

    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    #! w_+2 
    #! w_-2
    #! w_+3
    #! w_-3
    ppc["gencost"] = array([
        [2, 1500, 0, 3, 0.11,   5,   150, 10,   10, 1,  1],
        [2, 2000, 0, 3, 0.085,  1.2, 600, 1,    1,  1,  1],
        [2, 3000, 0, 3, 0.1225, 1,   335, 1,    1,  1,  1]
    ])

    return ppc


