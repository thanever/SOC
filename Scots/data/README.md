
## Case data

Four transmission networks are used for the case study, i.e., the IEEE 14-bus system, IEEE 30-bus system, IEEE 57-bus system, and 50Hertz control area of German transmission network (DE-50Hz). The DE-50Hz system is the 380 and 220 kV transmission network in the north-eastern Germany that is controlled by operator 50Hertz. We use the system data of German transmission network from [SciGRID](https://www.pypsa.org/examples/scigrid-lopf-then-pf.html), where the DE-50Hz system contains 76 buses, 166 lines, 16 transformers, and 265 generators. Detailed system data is given by [case14.py](./case14.py), [case30.py](./case30.py), [case14.py](./case57.py), and [case_de.py](./case_de.py), which are fomred by augmenting the [initial pypower data](./initial) with extra parameters for security-constrained optimal transmission switching problems (SCOTS) and the contingency set used for stochastic SCOTS. Please see [caseformat.py](./caseformat.py) for details on the case file format. 




<p align="center">
  <img alt="IEEE 14-bus system" title="IEEE 14-bus system" src="case14.png" width = "400" height = "400"/><img alt="IEEE 30-bus system" title="IEEE 30-bus system" src="case30.png" width = "400" height = "400" /> 
  <img alt="IEEE 57-bus system" title="IEEE 57-bus system" src="case57.png" width = "400" height = "400" /><img alt="The 50Hertz control area of the German transmission network" title="The 50Hertz control area of the German transmission network" src="case_de.png" width = "400" height = "400" /> 
</p>


<img src="http://latex.codecogs.com/gif.latex?\boldsymbol{x}" />
