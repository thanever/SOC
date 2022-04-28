
## Case data

Four transmission networks are used for the case study, i.e., the IEEE 14-bus system, IEEE 30-bus system, IEEE 57-bus system, and 50Hertz control area of German transmission network (DE-50Hz). The DE-50Hz system is the 380 and 220 kV transmission network in the north-eastern Germany that is controlled by operator 50Hertz. We use the system data of German transmission network from [SciGRID](https://www.pypsa.org/examples/scigrid-lopf-then-pf.html), where the DE-50Hz system contains 76 buses, 166 lines, 16 transformers, and 265 generators. Detailed system data is given by [case14.py](./case14.py), [case30.py](./case30.py), [case14.py](./case57.py), and [case_de.py](./case_de.py), which are fomred by augmenting the [initial pypower data](./initial) with extra parameters for security-constrained optimal transmission switching problems (SCOTS) and the contingency set used for stochastic SCOTS. Please see [caseformat.py](./caseformat.py) for details on the case file format. 


<p align="center">
  <img alt="IEEE 14-bus system" title="IEEE 14-bus system" src="case14.png" width = "400" height = "400"/><img alt="IEEE 30-bus system" title="IEEE 30-bus system" src="case30.png" width = "400" height = "400" /> 
  <img alt="IEEE 57-bus system" title="IEEE 57-bus system" src="case57.png" width = "400" height = "400" /><img alt="The 50Hertz control area of the German transmission network" title="The 50Hertz control area of the German transmission network" src="case_de.png" width = "400" height = "400" /> 
</p>

## Example of SCOTS formulation using the DC power flow model

The two-stage DR formulation of SCOTS can be written as 
<p align="center">
  <img src="eq-1.png" width=45%/> 
</p>
where <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{x}=[\boldsymbol{p}_{\rm{g_+}}^T,\boldsymbol{p}_{\rm{g_-}}^T,\boldsymbol{p}_{\rm{d}_{\Delta}}^T,\boldsymbol{z}_{+}^T,\boldsymbol{z}_{-}^T]^T">, and the first and second stages are the dispatch problem under the normal state and corrective control problem after a contingency, respectively. The first-stage objective function <img src="http://latex.codecogs.com/gif.latex?f(x)"> is the total generation cost, which is linearized using the ``<img src="http://latex.codecogs.com/gif.latex?\lambda">'' approximation in [1]. The second-stage objective function <img src="http://latex.codecogs.com/gif.latex?g(x)"> is the total cost of generator regulation, load shedding and corrective line switching, given by
<p align="center">
  <img src="eq-2.png" width=45%/> 
</p>
By adopting the DC power flow model, the first-stage feasible region
<p align="center">
  <img src="eq-3.png" width=38%/> 
</p>
which is defined by power flow and power balance constraints, and bound constraints of power outputs of generators, branch powers, and angle differences of branches. 
The second-stage feasible region 
<p align="center">
  <img src="eq-4.png" width=45%/> 
</p>
which is defined by the constraints analogous to those in <img src="http://latex.codecogs.com/gif.latex?\mathcal{X}"> but for the post-control system, bound constraints for regulation of generators and load shedding, constraints for switching actions, and constraints connecting topology, switching actions and branch contingencies. 

Notations used in the above formulation are listed in the following table (bold lowercase letters are all vectors with proper dimension):
|   |   |
|---|---|
|<img src="http://latex.codecogs.com/gif.latex?M">| Big-M constant.
|<img src="http://latex.codecogs.com/gif.latex?n_{\rm n}, n_{\rm g}, n_{\rm b}">| Numbers of buses, generators, and branches.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm g}, \bar{\boldsymbol{p}}_{\rm g}">| Active power outputs of generators and the counterpart of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm g}"> for the post-control system.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm d}, \bar{\boldsymbol{p}}_{\rm d}">| Active load powers and the counterpart of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm d}"> for the post-control system.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm b}, \bar{\boldsymbol{p}}_{\rm b}">| Active powers of branches and the counterpart of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm b}"> for the post-control system.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{\theta}, \bar{\boldsymbol{\theta}}">| Voltage phase angles of buses and the counterpart of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{\theta}"> for the post-control system.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{z}, \bar{\boldsymbol{z}}">| Statuses of branches where entry values of 1/0 denote the associated branches are switched on/off, counterpart of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{z}"> for the post-control topology.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm g}^{\rm{max}}">| Maximum active power outputs of generators. 
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{\theta}_{\rm max}">| Maximum phase angle difference of branches.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm b}^{\rm{max}}">| Power capacity of branches.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{{\rm g}_+}, \boldsymbol{p}_{\rm{g}_-}">| Upward/downward regulations of active power outputs of generators. 
|<img src="http://latex.codecogs.com/gif.latex?{\boldsymbol{r}}_{\rm{g}_+}, {\boldsymbol{r}}_{\rm g_-}">| Upward/downward ramp rate of generators.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{p}_{\rm d_{\Delta}}, \boldsymbol{p}_{\rm d_{\Delta}}^{\rm max}">| Amount of load shedding and its upper bound.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{z}_{+}, \boldsymbol{z}_{-}">| Action signs of switching on/off branches. An entry value of 1/0 means a/no switching action performed.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{o}">| Parameterization of N-k contingencies. Entry values of 1/0 indicate the normal/failure state of components.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{o}_{\rm g}, \boldsymbol{o}_{\rm b}">| Sub-vectors of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{o}"> for generators and branches.
|<img src="http://latex.codecogs.com/gif.latex?\mathcal{X}, \mathcal{Z}(\cdot)">| Feasible region of the first/second-stage problem.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{E}_{\rm g}">| Incidence matrix between buses and generators.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{E}_{\rm d}">| Incidence matrix between buses and loads.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{E}">| Oriented incidence matrix of the underlying graph of the transmission network with each branch assigned arbitrary and fixed orientation.
|<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{B}">| Diagonal matrix formed by susceptance of each branch
|<img src="http://latex.codecogs.com/gif.latex?f(\cdot), g(\cdot)">| The first-stage and second-stage functions.
|<img src="http://latex.codecogs.com/gif.latex?P, \mathcal{P}">| Probability distribution of <img src="http://latex.codecogs.com/gif.latex?\boldsymbol{o}"> and its ambiguity set.



 

[1] C. Coffrin, B. Knueven, J. Holzer, and M. Vuffray, “The impacts of convex piecewise linear cost formulations on AC optimal power flow,” Electric Power Systems Research, vol. 199, p. 107191, Oct. 2021.

