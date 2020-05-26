from pypower.api import makeYbus, runpf, loadcase, ext2int, ppoption, rundcpf
import numpy as np
import scipy as sp
from copy import deepcopy
from os.path import dirname, join
import networkx as nx
from numpy.linalg import inv, multi_dot
import gurobipy as gp
from gurobipy import GRB
import cvxpy as cp
import math 
import random
import pickle
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

np.set_printoptions(linewidth=350)
np.set_printoptions(threshold=np.inf)

class DcOts:
    def __init__(self, path_casedata):
        self.path_casedata = path_casedata
        self._get_param()

    def _get_param(self):
        ## load data file
        self.casedata = loadcase(self.path_casedata)

        ## number data
        self.n_bus    = self.casedata['bus'].shape[0] # number of buses
        self.n_gen    = self.casedata['gen'].shape[0] # number of buses
        self.n_branch = self.casedata['branch'].shape[0] # number of branches

        ## map from the number of bus to the index of bus in ['bus']
        self.map_bus_bus = dict(zip(self.casedata['bus'][:, 0], range(0, self.n_bus)))  # number of bus -> index of bus in ['bus']
        self.map_branch_branch = dict()
        self.map_branch_branch.update( dict(zip([tuple(i) for i in self.casedata['branch'][:,0:2]], range(self.n_branch))) ) 
        self.map_branch_branch.update( dict(zip([tuple(i) for i in self.casedata['branch'][:,[1,0]]], range(self.n_branch))) )# branch -> index of branch in ['branch']
 
        ## limit data
        self.p_g_max  = np.expand_dims(self.casedata['gen'][:, 8]/self.casedata["baseMVA"], axis = 1)
        self.p_g_min  = np.expand_dims(self.casedata['gen'][:, 9]/self.casedata["baseMVA"], axis = 1)
        self.p_b_max  = np.expand_dims(self.casedata['branch'][:, 5]/self.casedata["baseMVA"], axis = 1)
        self.p_b_min  = - self.p_b_max
 
        ## load data 
        self.p_l = np.expand_dims(self.casedata['bus'][:,2]/self.casedata["baseMVA"], axis = 1)

        ## run the power flow
        # opt = ppoption(PF_TOL=1e-12, PF_MAX_IT= 20)
        # self.result_pf = rundcpf(self.casedata,opt)

        ## reactance data
        pcc_y = ext2int(self.casedata)     
        Y_bus = makeYbus(pcc_y["baseMVA"], pcc_y["bus"], pcc_y["branch"])[0].toarray()
        self.B_bus = np.imag(Y_bus)
        self.B_branch = np.diag([self.B_bus[self.map_bus_bus[i], self.map_bus_bus[j]] for (i,j) in self.casedata['branch'][:, 0: 2]])

        ## Create the graph of the power system and its incidence matrix
        G = nx.DiGraph()
        G.add_nodes_from(self.casedata['bus'][:,0])
        G.add_edges_from([tuple(i) for i in self.casedata['branch'][:,0:2]])
        self.E_G = - np.array(
            nx.incidence_matrix(
                G, oriented=True, edgelist = [tuple(i) for i in self.casedata['branch'][:,0:2]]).todense())  # the head of edges in the nx function is the to bus of branches, so product -1

        ## Minimum spanning tree of the original network. Branches in the spanning tree are assumed to be on and unswitchable.
        G_und = nx.Graph()
        G_und.add_nodes_from(self.casedata['bus'][:,0])
        G_und.add_edges_from([tuple(i) for i in self.casedata['branch'][:,0:2]])
        for i in G_und.edges: G_und.edges[i]['weight'] = self.casedata['branch'][ self.map_branch_branch[i], 3] 
        self.G_sptree = nx.minimum_spanning_tree(G_und, weight='weight')
        self.ind_branch_sptree = [self.map_branch_branch[i] for i in self.G_sptree.edges] # index of branch in the spanning tree

        ## Transfer matrix 
        self.T_g = np.zeros((self.n_bus, self.n_gen))  # T_g @ p_g = [0, p_g[j],... p_g[i], 0...].T
        for i_gen in self.casedata['gen'][:, 0]:
            self.T_g[ np.where(self.casedata['bus'][:, 0] == i_gen )[0][0], np.where(self.casedata['gen'][:,0] == i_gen )[0] ] = 1

        ## parameters for model comparison
        self.ratio_switchable = [0.3, 0.4, 0.5, 0.6, 0.7]  # \alpha in the paper
        self.n_line_config = 50 # number of line configuration
        self.n_repeat = 50 # number of repeating for averaging
        self.i_models = [0, 1, 2, 3] # set of OTS model


    def reduction(self, index_unswitch):
        '''
        parameters for reduced connectedness constriants 
        '''

        G_fixed = nx.Graph()     # graph by all unswitchable lines in branch_load
        G_fixed.add_edges_from( self.casedata['branch'][ index_unswitch , 0: 2] )  # add lines which are unswitchable
        GG_sub = [G_fixed.subgraph(c).copy() for c in nx.connected_components( G_fixed )]  

        ind_bc_connect = set() # indx set of switchable branches connecting any two subgraphs in GG_sub
        ind_bc_contain = set() # idnx set of switchable branches contained in any subgraph in GG_sub
        for i in range(self.n_branch):
            bc = self.casedata['branch'][i, 0:2]
            for G in GG_sub:
                if bc[0] in G.nodes and bc[1] in G.nodes:
                    ind_bc_contain.add( i )
                    break

        ind_bc_connect = list( set(range(self.n_branch)) - ind_bc_contain ) # invert to list which is ordered
        bus_connect = set() # set of buses of all branches in ind_bc_connect
        for i in ind_bc_connect:
            bus_connect.add( self.casedata['branch'][i][0] )
            bus_connect.add( self.casedata['branch'][i][1] )

        GG_node = dict()  # set of node which connected with branches in ind_bc_connect, for each graph in GG_sub
        branch_aux = list()  # auxiliry branch added 
        for G in GG_sub:
            GG_node[G] = set()
            for i in G.nodes:
                if i in bus_connect:
                    GG_node[G].add(i)

            GG_node[G] = list(GG_node[G])
            if len(GG_node[G]) == 1:
                None
            elif len(GG_node[G]) > 1:
                for i in range(len(GG_node[G]) - 1):
                    branch_aux.append( (GG_node[G][i], GG_node[G][i+1]) )
            else:
                print("Grpah error")

        # reduced graph 
        G_reduce = nx.DiGraph() 
        G_reduce.add_edges_from([ self.casedata['branch'][i][0:2]  for i in ind_bc_connect ] + branch_aux  )
        E_G_reduce = - np.array(nx.incidence_matrix(G_reduce, oriented=True, edgelist = [ self.casedata['branch'][i][0:2]  for i in ind_bc_connect ] + branch_aux ).todense())  # the head of edges in the nx function is the to bus of branches, so -1
        n_reduce = E_G_reduce.shape[0]  #number of nodes in G_reduce

        # parameters used in the connectedness constraint
        self.n_reduce_fixed = len(branch_aux)  # number of branches which are  fixed in graph G_reduce
        self.ind_bc_connect = ind_bc_connect
        self.E_G_reduce = E_G_reduce
        self.n_bus_reduce = n_reduce
        self.n_branch_reduce = len(ind_bc_connect) + self.n_reduce_fixed       

    def opt(self, index_unswitch, i_model):
        '''
        branch_unswitch - index of branches which are unswitchable
        i_model - = 0 the original DC OTS； =1 with necessary connectedness constraints; =2 with the proposed constraints; = 3 with the reduced constraints
        '''

        cont_redc = [[False, False], [False, True], [True, False], [True, True]]
        connectedness, reduce = cont_redc[i_model][0], cont_redc[i_model][1]

        ## Parameters
        M = 500  # 5000 for case300
        ## Optimization variables
        theta = cp.Variable((self.n_bus, 1))
        p_g = cp.Variable((self.n_gen, 1)) # p.u.
        z = cp.Variable((self.n_branch, 1), boolean=True)
        p_b = cp.Variable((self.n_branch, 1))

        if connectedness == True: 
            # for ensuring connectedness
            if reduce == False:
                n_bus_aux = self.n_bus
                n_branch_aux = self.n_branch
                z_aux = z
                E_G_aux = deepcopy(self.E_G)

            elif reduce == True:
                self.reduction(index_unswitch)
                n_bus_aux = self.n_bus_reduce
                n_branch_aux = self.n_branch_reduce
                E_G_aux = self.E_G_reduce
                z_aux = cp.vstack([z[self.ind_bc_connect], np.ones((self.n_reduce_fixed, 1)) ])

            c =   np.expand_dims( np.ones(n_bus_aux), axis = 1)
            c[-1] = - np.sum(c[:-1])

            vartheta = cp.Variable((n_bus_aux, 1))
            rho = cp.Variable((n_branch_aux, 1))
                 
        ## Add constraints
        # angle limit
        constraints = []
        constraints += [ theta <= np.pi  ]
        constraints += [ theta >= - np.pi ]
        # generation power limit
        constraints += [ p_g <= self.p_g_max ]
        constraints += [ p_g >= self.p_g_min ]
        # branch power limit
        constraints += [ p_b <= np.diag(self.p_b_max) @ z ] 
        constraints += [ p_b >= np.diag(self.p_b_min) @ z ]
        # node power balance
        constraints += [ self.E_G @ p_b +  self.p_l == self.T_g @ p_g ]

        # branch power equation
        constraints += [ self.B_branch @ self.E_G.T @ theta - p_b + M * (1 - z) >= 0 ]
        constraints += [ self.B_branch @ self.E_G.T @ theta - p_b - M * (1 - z) <= 0 ]
        # reference bus
        constraints += [ theta[0] == 0 ]

        # switching constraints
        constraints += [ z[index_unswitch] == 1 ]
        constraints += [ cp.sum(z) >= math.ceil( 0.85 * self.n_branch  ) ]
        constraints += [ cp.sum(z) <= math.ceil( 0.95 * self.n_branch  ) ]

        if connectedness == True:  
            constraints += [  E_G_aux.T @ vartheta - rho + M * (1 - z_aux) >= 0 ]
            constraints += [  E_G_aux.T @ vartheta - rho - M * (1 - z_aux) <= 0 ]
            constraints += [  E_G_aux @ rho == c ]
            constraints += [ rho <=   M * z_aux ]
            constraints += [ rho >= - M * z_aux ]
            constraints += [ vartheta[0] == 0 ]

        if connectedness == False and reduce ==True:
            constraints += [ np.abs(self.E_G) @ z >= np.ones([self.n_bus, 1]) ]
 
        objective = cp.Minimize(  self.casedata['gencost'][:,-2] @ p_g )
        problem = cp.Problem(objective, constraints) 
        problem.solve(solver = 'GUROBI', verbose = False)

        self.status = problem.status
        self.solve_time = problem.solver_stats.solve_time
        self.z = z.value
        self.get_island()  # get self.n_island


    def get_island(self):

        G_opt = nx.Graph()     # graph by all unswitchable lines in branch_load
        G_opt.add_nodes_from( self.casedata['bus'][:, 0 ] )
        G_opt.add_edges_from( self.casedata['branch'][ np.where(case.z == 1)[0] , 0: 2] )  # add lines which are unswitchable
        G_island = [G_opt.subgraph(c).copy() for c in nx.connected_components( G_opt )]  
        self.n_island = len(G_island)

    def model_compare(self, path_opt_result):
        
        opt_result = dict() 
        for r_switchable in self.ratio_switchable:
            # randomly gnerate 50 switchable/unswitchable line configurations
            branch_unswitch = np.array([])                 
            for i in range(self.n_line_config):
                if i == 0 :
                    branch_unswitch = [np.array( random.sample(range(0, case.n_branch), case.n_branch - math.ceil( r_switchable * case.n_branch )))]
                else:
                    branch_unswitch = np.r_[ branch_unswitch, [np.array(random.sample( range(0, case.n_branch), case.n_branch - math.ceil( r_switchable * case.n_branch ) ) ) ]]
            for i_model in self.i_models:
                status, solve_time, n_island = [], [], []
                for i in range(self.n_line_config):
                    for j in range(self.n_repeat):
                        index_unswitch = branch_unswitch[i, :] 
                        case.opt(index_unswitch, i_model)
                        status.append(case.status)
                        solve_time.append(case.solve_time)
                        n_island.append(case.n_island)
                        print(r_switchable, i_model, i, j, case.status, case.solve_time, case.n_island)
                opt_result[i_model, r_switchable, 'status'] = status
                opt_result[i_model, r_switchable, 'solve_time'] = solve_time
                opt_result[i_model, r_switchable, 'n_island'] = n_island
            opt_result[r_switchable, 'branch_unswitch'] = branch_unswitch

        with open(path_opt_result, 'wb') as handle:
            pickle.dump(opt_result, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def plot_result(self, path_fig):

        plt.style.use( 'ggplot' ) #('seaborn-paper')
        plt.rc('text', usetex=True)
        plt.rc('font', size=8,family='serif') 
        plt.rcParams['ytick.major.width'] = 0
        plt.rcParams['xtick.major.width'] =0 
        plt.rcParams['lines.linewidth'] = 0.65

        T = dict()
        for casename in ['case30', 'case300']:
            path_casedata = join(dirname(__file__), 'data//casedata//'+ casename +'.py')
            path_opt_result = join(dirname(__file__), 'result//'+ casename +'.pickle')
            with open(path_opt_result, 'rb') as handle:
                opt_result = pickle.load(handle)
            T[casename] = np.zeros([len(self.ratio_switchable), len(self.i_models)])
            for i_model in self.i_models:
                for r in range(len(self.ratio_switchable)):
                    T[casename][r, i_model] = np.mean(opt_result[ i_model , self.ratio_switchable[r], 'solve_time'] )

        fig = plt.figure(tight_layout=True, figsize=(4, 1.5) )
        gs = GridSpec(1, 2, figure=fig)
        ax = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]) ]

        for i in range(4):
            ax[0].plot(R, T['case30'][:,i], marker = ['^','s','o','p'][i], markersize = 3.4, linewidth = 0.5)
        for i in range(4):
            ax[1].plot(R, T['case300'][:,i], marker = ['^','s','o','p'][i], markersize = 3.4, linewidth = 0.5)

        ax[0].set_xlim([0.285, 0.715])
        ax[0].set_xticks(R)
        ax[0].set_ylim([0.015, 0.025])
        ax[0].set_yticks([0.015, 0.0175, 0.020, 0.0225, 0.025  ])
        ax[0].tick_params(axis='x', pad = -2)
        ax[0].tick_params(axis='y', pad = -2)

        ax[1].set_xlim([0.285, 0.715])
        ax[1].set_xticks(R)
        ax[1].set_ylim([0.1, 0.5])
        ax[1].set_yticks([0.1, 0.2, 0.3, 0.4, 0.5  ])
        ax[1].tick_params(axis='x', pad = -2)
        ax[1].tick_params(axis='y', pad = -2)

        ax[0].set_xlabel('$\\alpha$', labelpad = 1)
        ax[1].set_xlabel('$\\alpha$', labelpad = 1)
        ax[0].set_ylabel('Average solution \n time (s)')

        ax[0].set_title('(a) IEEE 30-bus system', fontsize = 8)
        ax[1].set_title('(b) IEEE 300-bus system', fontsize = 8)

        ax[0].text(0.52, 0.0225, 'M3')
        ax[0].text(0.54, 0.02, 'M4')
        ax[0].text(0.5, 0.018, 'M1')
        ax[0].text(0.55, 0.0161, 'M2')
        ax[1].text(0.5, 0.42, 'M3')
        ax[1].text(0.51, 0.305, 'M4')
        ax[1].text(0.51, 0.208, 'M1')
        ax[1].text(0.51, 0.13, 'M2')
        
        fig.savefig(path_fig, bbox_inches='tight')



