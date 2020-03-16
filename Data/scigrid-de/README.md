The SciGRID network for Germany
---

This folder contains data of the SciGRID network for Germany. 

[./pypsa](./pypsa) contains CSV files in [PyPSA](https://pypsa.readthedocs.io/en/latest/index.html) format, which is a copy from http://www.pypsa.org/examples/scigrid-with-load-gen-trafos-2011.zip. Refer to https://www.pypsa.org/examples/scigrid-lopf-then-pf.html for more description of the data.


[./pypower](./pypower) contains .py files in [PYPOWER](https://github.com/rwl/PYPOWER/blob/master/pypower/caseformat.py) format. A total of 168 load snapshots from 12:00:00 AM January 3rd, 2011 to 11:00:00 PM January 9th, 2011 are converted here. Extra parameters for case studies of transmission switching to improve synchronization performance of low-inertia power grids are also included in the following format:

> Generator/Inverter Control Data Format - ["gen_control"]
>> 1.   bus number (positive integer)
>> 2.   generator/inverter type
>>         - synchronization generator = 1
>>         - gird-forming inverter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= 2
>>         - gird-forming inverter &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = 3
>> 3.   C{$m$}, inertia
>> 4.   C{$d$}, damping (MVAr)
>> 5.   C{$K_P$}, proportional synchronization gain
>> 6.   C{$K_I$}, integral synchronization gain
>> 7.   C{$\tau$}, filter time constant (s)

> Generation Mixture Data Format - ['gen_control_m']
>> {1: ["gen_control"]}, 100% grid-forming inverters
>> {2: ["gen_control"]}, 100% grid-following inverters
>> {3: ["gen_control"]}, hybrid

> Branch Data Format - ['branch_switch']
>> 1. to bus number
>> 2. from bus number
>> 3. switchableness of the branch, 0 denotes unswitchable and 1 denotes switchable

> Parameter Data Format - ['parameters']
>>  "x_trans_sg", transient reactance of synchronous generators (p.u., bMVA = maximum rate of the generator)
>>  "x_trans_fm", equivalent reactance of grid-forming inverters (p.u., bMVA = maximum rate of the inverter)
>>  "x_trans_fl", equivalent reactance of grid-following inverters (p.u., bMVA = maximum rate of the inverter)
>>  "d_l", damping of all load buses
>>  "d_l_perturb", perturbation of damping for buses with zero power injection
>>  "w_1_ij", weighting factor for phase cohesiveness
>>  "w_2_ij", weighting factor for frequency synchronization
>>  "w_3_ij", weighting factor for PLL-synchronization ($\Delta \hat{\theta}_i - \Delta \theta_j$)
>>  "w_4_ij", weighting factor for PLL-synchronization ($ \Delta \hat{\omega}_i$)
>>  "b_r", parameter for the lower bound of the total number of branches being switched on 
>>  "b_c", parameter for the upper bound of the total number of branches being switched on 