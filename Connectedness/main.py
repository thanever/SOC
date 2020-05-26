from os.path import dirname, join
from dc_ots import DcOts

for casename in ['case30', 'case300']:
    path_casedata = join(dirname(__file__), 'data//casedata//'+ casename +'.py')
    path_opt_result = join(dirname(__file__), 'result//'+ casename +'_model_copmare.pickle') # path of result file of model comparison
    case = DcOts(path_casedata) 
    case.model_compare(path_opt_result) 

# plot results of computation time
path_fig = join(dirname(__file__), 'result//' +'fig-0-1-1.pdf')
case.plot_result(path_fig)  
