"""Defines the case file format.
The case file is a Python file which inherits the format of the PYPOWER case file (see https://github.com/rwl/PYPOWER/blob/master/pypower/caseformat.py) and contains some additional data. 
=================================
 
Bus Data Format
---------------
  1.   bus number (positive integer)
  2.   bus type
          - PQ bus          = 1
          - PV bus          = 2
          - reference bus   = 3
          - isolated bus    = 4
  3.   C{Pd}, real power demand (MW)
  4.   C{Qd}, reactive power demand (MVAr)
  5.   C{Gs}, shunt conductance (MW demanded at V = 1.0 p.u.)
  6.   C{Bs}, shunt susceptance (MVAr injected at V = 1.0 p.u.)
  7.   area number, (positive integer)
  8.   C{Vm}, voltage magnitude (p.u.)
  9.   C{Va}, voltage angle (degrees)
  10.  C{baseKV}, base voltage (kV)
  11.  C{zone}, loss zone (positive integer)
  12.  C{maxVm}, maximum voltage magnitude (p.u.)
  13.  C{minVm}, minimum voltage magnitude (p.u.)
 +14.  ratio_ls_max, maximal ratio of load shedding
 +15.  w_d,  load shedding cost ($/MW)

Generator Data Format
---------------------
  1.   bus number
  2.   C{Pg}, real power output (MW)
  3.   C{Qg}, reactive power output (MVAr)
  4.   C{Qmax}, maximum reactive power output (MVAr)
  5.   C{Qmin}, minimum reactive power output (MVAr)
  6.   C{Vg}, voltage magnitude setpoint (p.u.)
  7.   C{mBase}, total MVA base of this machine, defaults to baseMVA
  8.   status,
           - C{>  0} - machine in service
           - C{<= 0} - machine out of service
  9.   C{Pmax}, maximum real power output (MW)
  10.  C{Pmin}, minimum real power output (MW)
  11.  C{Pc1}, lower real power output of PQ capability curve (MW)
  12.  C{Pc2}, upper real power output of PQ capability curve (MW)
  13.  C{Qc1min}, minimum reactive power output at Pc1 (MVAr)
  14.  C{Qc1max}, maximum reactive power output at Pc1 (MVAr)
  15.  C{Qc2min}, minimum reactive power output at Pc2 (MVAr)
  16.  C{Qc2max}, maximum reactive power output at Pc2 (MVAr)
  17.  ramp rate for load following/AGC (MW/min)
  18.  ramp rate for 10 minute reserves (MW)
  19.  ramp rate for 30 minute reserves (MW)
  20.  ramp rate for reactive power (2 sec timescale) (MVAr/min)
  21.  APF, area participation factor
 +22.  generator type, equal to 0 for conventional generators and 1 for VRE-based generators
 +23.  phi_v_min, minimal power factor of inverters
 +24.  s_v_max, MVA rating of inverters
 +25.  r_+2, upward ramp rate for the second stage
 +26.  r_-2, downward ramp rate for the second stage, r_-2 = r_+2 if the generator does not participate into regulation 
 +27.  r_+3, upward ramp rate for the second stage
 +28.  r_-3, downward ramp rate for the second stage, r_-3 = r_+3 if the generator does not participate into regulation

Branch Data Format
------------------
  1.   C{f}, from bus number
  2.   C{t}, to bus number
  3.   C{r}, resistance (p.u.)
  4.   C{x}, reactance (p.u.)
  5.   C{b}, total line charging susceptance (p.u.)
  6.   C{rateA}, MVA rating A (long term rating)
  7.   C{rateB}, MVA rating B (short term rating)
  8.   C{rateC}, MVA rating C (emergency rating)
  9.   C{ratio}, transformer off nominal turns ratio ( = 0 for lines )
  10.  C{angle}, transformer phase shift angle (degrees), positive => delay
       (Gf, shunt conductance at from bus p.u.)
       (Bf, shunt susceptance at from bus p.u.)
       (Gt, shunt conductance at to bus p.u.)
       (Bt, shunt susceptance at to bus p.u.)
  11.  initial branch status, 1 - in service, 0 - out of service
  12.  minimum angle difference, angle(Vf) - angle(Vt) (degrees)
  13.  maximum angle difference, angle(Vf) - angle(Vt) (degrees)
 +14.  w_s, cost of line switching in the third-stage corrective control ($)

Generator Cost Data Format
--------------------------
NOTE: If C{gen} has C{ng} rows, then the first C{ng} rows of gencost contain
the cost for active power produced by the corresponding generators.
If C{gencost} has 2*ng rows then rows C{ng+1} to C{2*ng} contain the reactive
power costs in the same format.
  1.   C{model}, 1 - piecewise linear, 2 - polynomial
  2.   C{startup}, startup cost in US dollars
  3.   C{shutdown}, shutdown cost in US dollars
  4.   C{N}, number of cost coefficients to follow for polynomial
       cost function, or number of data points for piecewise linear
  5.   and following, parameters defining total cost function C{f(p)},
       units of C{f} and C{p} are $/hr and MW (or MVAr), respectively.
       (MODEL = 1) : C{p0, f0, p1, f1, ..., pn, fn}
       where C{p0 < p1 < ... < pn} and the cost C{f(p)} is defined by
       the coordinates C{(p0,f0), (p1,f1), ..., (pn,fn)} of the
       end/break-points of the piecewise linear cost function
       (MODEL = 2) : C{cn, ..., c1, c0}
       C{n+1} coefficients of an C{n}-th order polynomial cost function,
       starting with highest order, where cost is
       C{f(p) = cn*p^n + ... + c1*p + c0}
 +6.   w_+2, upward regulation cost at the second-stage ($/MW)
 +7.   w_-2, downward regulation cost at the second-stage ($/MW)
 +8.   w_+3, upward regulation cost at the third-stage ($/MW)
 +9.   w_-3, downward regulation cost at the third-stage ($/MW)
"""
 