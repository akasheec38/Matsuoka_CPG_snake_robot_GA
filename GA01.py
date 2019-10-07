# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:59:16 2019

@author: MOC817
"""

import numpy as np 
import CPG_osc
import VREP_com
from log import log
import vrep
from constants import NUM_OF_OSC




def cal_pop_fitness(clientID, Handle, pop, fixed_CPG_array):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function caulcuates the total distance travelled towards a target 
         
    fitness = []
    for i in range(pop.shape[0]):
        VREP_com.vrep_sim_check(clientID)
        vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
        vrep.simxSynchronousTrigger(clientID)    
        VREP_com.vrep_reset_robot_joints(clientID, Handle)
        vrep.simxSynchronousTrigger(clientID)
        vrep.simxGetPingTime(clientID)
        log('[GA] Logging Genes of Chromosome {0} for tau, beta, w_0, u_e, kf for each CPGs---'.format(i))
        if pop.shape[1] == 48:
            log('[GA] tau_1 = {0} ,tau_prime_1 = {1} ,beta_1 = {2} ,w_0_1 = {3} ,u_e_1 = {4} ,kf_1 = {5} '.format(pop[i][0], 
                                pop[i][1],pop[i][2],pop[i][3],pop[i][4],pop[i][5]))
            log('[GA] tau_2 = {0}  ,tau_prime_2 = {1} ,beta_2 = {2} ,w_0_2 = {3} ,u_e_2 = {4} ,kf_2 = {5} '.format(pop[i][6], 
                                pop[i][7],pop[i][8],pop[i][9],pop[i][10],pop[i][11]))
            log('[GA] tau_3 = {0} ,tau_prime_3 = {1} ,beta_3 = {2} ,w_0_3 = {3} ,u_e_3 = {4} ,kf_3 = {5}  '.format(pop[i][12], 
                                pop[i][13],pop[i][14],pop[i][15],pop[i][16],pop[i][17]))
            log('[GA] tau_4 = {0} ,tau_prime_4 = {1} ,beta_4 = {2} ,w_0_4 = {3} ,u_e_4 = {4} ,kf_4 = {5}  '.format(pop[i][18], 
                                pop[i][19],pop[i][20],pop[i][21],pop[i][22],pop[i][23]))
            
            log('[GA] tau_5 = {0} ,tau_prime_5 = {1} ,beta_5 = {2} ,w_0_5 = {3} ,u_e_5 = {4} ,kf_5 = {5} '.format(pop[i][24], 
                                pop[i][25],pop[i][26],pop[i][27],pop[i][28],pop[i][29]))
            log('[GA] tau_6 = {0}  ,tau_prime_6 = {1} ,beta_6 = {2} ,w_0_6 = {3} ,u_e_6 = {4} ,kf_6 = {5} '.format(pop[i][30], 
                                pop[i][31],pop[i][32],pop[i][33],pop[i][34],pop[i][35]))
            log('[GA] tau_7 = {0} ,tau_prime_7 = {1} ,beta_7 = {2} ,w_0_7 = {3} ,u_e_7 = {4} ,kf_7 = {5}  '.format(pop[i][36], 
                                pop[i][37],pop[i][38],pop[i][39],pop[i][40],pop[i][41]))
            log('[GA] tau_8 = {0} ,tau_prime_8 = {1} ,beta_8 = {2} ,w_0_8 = {3} ,u_e_8 = {4} ,kf_8 = {5}  '.format(pop[i][42], 
                                pop[i][43],pop[i][44],pop[i][45],pop[i][46],pop[i][47]))
            log('[GA] w_21 = {0} ,w_32 = {1} ,w_43 = {2}, w_51 = {3} ,w_65 = {4} ,w_76 = {5}, w_87 = {6} '.format( fixed_CPG_array[0], fixed_CPG_array[1],fixed_CPG_array[2],
                                                                                                                    fixed_CPG_array[3], fixed_CPG_array[4],fixed_CPG_array[5],fixed_CPG_array[6]))
        if pop.shape[1] == 3:
            log('[GA] tau_1 = {0} ,tau_prime_1 = {1} ,beta_1 = {2} ,w_0_1 = {3} ,u_e_1 = {4} ,kf_1 = {5}'.format(fixed_CPG_array[0][0][0],
                fixed_CPG_array[0][0][1],fixed_CPG_array[0][0][2], fixed_CPG_array[0][0][3], fixed_CPG_array[0][0][4], fixed_CPG_array[0][0][5]))
            log('[GA] tau_2 = {0}  ,tau_prime_2 = {1} ,beta_2 = {2} ,w_0_2 = {3} ,u_e_2 = {4} ,kf_2 = {5} '.format(fixed_CPG_array[0][0][6],
                fixed_CPG_array[0][0][7],fixed_CPG_array[0][0][8], fixed_CPG_array[0][0][9], fixed_CPG_array[0][0][10], fixed_CPG_array[0][0][11]))
            log('[GA] tau_3 = {0} ,tau_prime_3 = {1} ,beta_3 = {2} ,w_0_3 = {3} ,u_e_3 = {4} ,kf_3 = {5} '.format(fixed_CPG_array[0][0][12],
                fixed_CPG_array[0][0][13],fixed_CPG_array[0][0][14], fixed_CPG_array[0][0][15], fixed_CPG_array[0][0][16], fixed_CPG_array[0][0][17]))
            log('[GA] tau_4 = {0} ,tau_prime_4 = {1} ,beta_4 = {2} ,w_0_4 = {3} ,u_e_4 = {4} ,kf_4 = {5} '.format(fixed_CPG_array[0][0][18],
                fixed_CPG_array[0][0][19],fixed_CPG_array[0][0][20], fixed_CPG_array[0][0][21], fixed_CPG_array[0][0][22], fixed_CPG_array[0][0][23]))
            
            log('[GA] tau_5 = {0} ,tau_prime_5 = {1} ,beta_5 = {2} ,w_0_5 = {3} ,u_e_5 = {4} ,kf_5 = {5} '.format(fixed_CPG_array[0][0][24],
                fixed_CPG_array[0][0][25],fixed_CPG_array[0][0][26], fixed_CPG_array[0][0][27], fixed_CPG_array[0][0][28], fixed_CPG_array[0][0][29]))
            log('[GA] tau_6 = {0}  ,tau_prime_6 = {1} ,beta_6 = {2} ,w_0_6 = {3} ,u_e_6 = {4} ,kf_6 = {5} '.format(fixed_CPG_array[0][0][30],
                fixed_CPG_array[0][0][31],fixed_CPG_array[0][0][32], fixed_CPG_array[0][0][33], fixed_CPG_array[0][0][34], fixed_CPG_array[0][0][35]))
            log('[GA] tau_7 = {0} ,tau_prime_7 = {1} ,beta_7 = {2} ,w_0_7 = {3} ,u_e_7 = {4} ,kf_7 = {5}  '.format(fixed_CPG_array[0][0][36],
                fixed_CPG_array[0][0][37],fixed_CPG_array[0][0][38], fixed_CPG_array[0][0][39], fixed_CPG_array[0][0][40], fixed_CPG_array[0][0][41]))
            log('[GA] tau_8 = {0} ,tau_prime_8 = {1} ,beta_8 = {2} ,w_0_8 = {3} ,u_e_8 = {4} ,kf_8 = {5}  '.format(fixed_CPG_array[0][0][42],
                fixed_CPG_array[0][0][43],fixed_CPG_array[0][0][44], fixed_CPG_array[0][0][45], fixed_CPG_array[0][0][46], fixed_CPG_array[0][0][47]))
            log('[GA] w_21 = {0} ,w_32 = {1} ,w_43 = {2}, w_51 = {3} ,w_65 = {4} ,w_76 = {5}, w_87 = {6} '.format( pop[i][0], pop[i][1],pop[i][2], pop[i][3], pop[i][4],pop[i][5], pop[i][6]))
            
        log('[GA] Running simulation on VREP -  Getting Fitness of Chromosome {0}'.format(i)) 
                  
        osc1_out_val, osc2_out_val, osc3_out_val, osc4_out_val, osc5_out_val, osc6_out_val, osc7_out_val, osc8_out_val= CPG_osc.CPG_network(pop[i][:], fixed_CPG_array)
        
        for i in range(len(osc1_out_val)):
            OSC_Outputs = []        
            OSC_Outputs.append(osc1_out_val[i])
            OSC_Outputs.append(osc2_out_val[i])
            OSC_Outputs.append(osc3_out_val[i])
            OSC_Outputs.append(osc4_out_val[i])
            
            OSC_Outputs.append(osc5_out_val[i])
            OSC_Outputs.append(osc6_out_val[i])
            OSC_Outputs.append(osc7_out_val[i])
            OSC_Outputs.append(osc8_out_val[i])
            
            
            VREP_com.vrep_moves_robot(clientID, Handle, np.array(OSC_Outputs))         
            vrep.simxSynchronousTrigger(clientID)
            vrep.simxGetPingTime(clientID)        
            del OSC_Outputs
        ## Considering its Y position only
        err_code, MyRobotPos_Current = vrep.simxGetObjectPosition(clientID, Handle[0, 0], -1, vrep.simx_opmode_blocking)
        MyRobotPos_Current = np.array(MyRobotPos_Current)
        fitness.append(MyRobotPos_Current[1])
        vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)  
    #print('fitness......................', fitness)
    return fitness

def select_mating_pool(pop, fitness, num_parents):
    print('fitness: ', fitness)
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        #print('max_fitness_idx: ', max_fitness_idx)
        max_fitness_idx = max_fitness_idx[0][0]
        #print('max_fitness_idx: ', max_fitness_idx)
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = np.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 2] = offspring_crossover[idx, 2] + random_value
    return offspring_crossover
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
