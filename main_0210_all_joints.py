# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:26:02 2019

@author: MOC817
"""
import vrep
import numpy as np
import CPG_osc
#import VREP_com
import time
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
#import GA01
#from log import Logger, log, excel_logger
import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')

from constants import TOT_NUM_OF_PARAM,  NUM_PARENTS_MATING, SOL_PER_POP, FIRST_ITER_GEN, FIRST_ITER_NUM_OF_PARAM, NUM_OF_GEN, NUM_OF_OSC
from constants import MIN_beta, MIN_kf, MIN_tau, MIN_tau_prime, MIN_u_e, MIN_w_0, MIN_w_21, MIN_w_32, MIN_w_43, MIN_w_51, MIN_w_65, MIN_w_76, MIN_w_87
from constants import MAX_beta, MAX_kf, MAX_tau, MAX_tau_prime, MAX_u_e, MAX_w_0, MAX_w_21, MAX_w_32, MAX_w_43, MAX_w_51, MAX_w_65, MAX_w_76, MAX_w_87

#%%
'''
clientID = VREP_com.clientID
Handle = VREP_com.Handle
VREP_com.vrep_sim_check(clientID)

#%%
# Set the home directory
home_dir = os.path.expanduser('E:\LabWork\Vrep\main_work\Fresh_CPG\Snake_trainCPG_para_itretivily\Snake_Train_All_CPG_with_diff_param\Snake_4_Joints\Snake_0210')
# Set the logging variables
# This also creates a new log file
Logger(log_dir=os.path.join(home_dir, 'snake_run\logs\''), log_flag=True)

'''
#%%
print('Which mode you want to run -- GA(1)/ Simple CPG(2)      ')
mode = int(input("Enter mode want to run GA = 1, Simple CPG = 2:  "))
#print(mode)
if (mode == 1):
    ##"run Genetic algorithm"
    print("Connecting to Genetic Algorithm framwork for Optimising CPG parametrs    ")
    # Create the position bounds of the individual
    #######################################################################################################################
    ###################################  optimising - tau, tau_prime, beta, w_0, u_e, kf..... #############################
    #######################################################################################################################
    log('[GA] Creating position bounds for optimising - tau, tau_prime, beta, w_0, u_e, kf.....')
    log('[GA] Logging position bounds')
    log('[GA] MIN_tau={0}, MAX_tau={1}'.format(MIN_tau, MAX_tau))
    log('[GA] MIN_tau_prime={0}, MAX_tau_prime={1}'.format(MIN_tau_prime, MAX_tau_prime))
    log('[GA] MIN_beta={0}, MAX_beta={1}'.format(MIN_beta, MAX_beta))
    log('[GA] MIN_w_0={0}, MAX_w_0={1}'.format(MIN_w_0, MAX_w_0))
    log('[GA] MIN_u_e={0}, MAX_u_e={1}'.format(MIN_u_e, MAX_u_e))
    log('[GA] MIN_kf={0}, MAX_kf={1}'.format(MIN_kf, MAX_kf))            
    #%% (GA)
    # Defining the population size.
    pop_size = (SOL_PER_POP,FIRST_ITER_NUM_OF_PARAM)    
    #Creating the initial population.
    new_population = [[0 for x in range(FIRST_ITER_NUM_OF_PARAM)] for y in range(SOL_PER_POP)] 
    #new_population = matrix[SOL_PER_POP][NUM_OF_PARAM]
    for i in range(pop_size[0]):
        new_population[i][0] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][1] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][2] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][3] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][4] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][5] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][6] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][7] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][8] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][9] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][10] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][11] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][12] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][13] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][14] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][15] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][16] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][17] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][18] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][19] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][20] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][21] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][22] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][23] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][24] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][25] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][26] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][27] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][28] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][29] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][30] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][31] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][32] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][33] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][34] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][35] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][36] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][37] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][38] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][39] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][40] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][41] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
        new_population[i][42] = round(np.random.uniform(low=MIN_tau, high=MAX_tau), 2)
        new_population[i][43] = round(np.random.uniform(low=MIN_tau_prime, high=MAX_tau_prime), 2)
        new_population[i][44] = round(np.random.uniform(low=MIN_beta, high=MAX_beta), 2)
        new_population[i][45] = round(np.random.uniform(low=MIN_w_0, high=MAX_w_0), 2)
        new_population[i][46] = round(np.random.uniform(low=MIN_u_e, high=MAX_u_e), 2)
        new_population[i][47] = round(np.random.uniform(low=MIN_kf, high=MAX_kf), 2)
        
            
            
    new_population = np.array(new_population)
    log('[GA] Starting genetic algorithm for optimising - tau, tau_prime, beta, w_0, u_e, kf.....')
    for generation in range(FIRST_ITER_GEN):        
        log('[GA] Running generation {0}'.format(generation))  
        fixed_CPG_array = [-1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0] 
        fitness = GA01.cal_pop_fitness(clientID, Handle, new_population, fixed_CPG_array)
        ## Saving logs in excel file 
        df = pd.DataFrame({ 'Chromosome ID' : [(i+1) for i in range(new_population.shape[0])],
                            'tau_1':new_population[:,0],
                            'tau_prime_1':new_population[:,1],
                            'beta_1':new_population[:,2],
                            'w_0_1':new_population[:,3],
                            'u_e_1':new_population[:,4],
                            'kf_1':new_population[:,5],
                            'tau_2':new_population[:,6],
                            'tau_prime_2':new_population[:,7],
                            'beta_2':new_population[:,8],
                            'w_0_2':new_population[:,9],
                            'u_e_2':new_population[:,10],
                            'kf_2':new_population[:,11],
                            'tau_3':new_population[:,12],
                            'tau_prime_3':new_population[:,13],
                            'beta_3':new_population[:,14],
                            'w_0_3':new_population[:,15],
                            'u_e_3':new_population[:,16],
                            'kf_3':new_population[:,17],
                            'tau_4':new_population[:,18],
                            'tau_prime_4':new_population[:,19],
                            'beta_4':new_population[:,20],
                            'w_0_4':new_population[:,21],
                            'u_e_4':new_population[:,22],
                            'kf_4':new_population[:,23],
                            'tau_5':new_population[:,24],
                            'tau_prime_5':new_population[:,25],
                            'beta_5':new_population[:,26],
                            'w_0_5':new_population[:,27],
                            'u_e_5':new_population[:,28],
                            'kf_5':new_population[:,29],
                            'tau_6':new_population[:,30],
                            'tau_prime_6':new_population[:,31],
                            'beta_6':new_population[:,32],
                            'w_0_6':new_population[:,33],
                            'u_e_6':new_population[:,34],
                            'kf_6':new_population[:,35],
                            'tau_7':new_population[:,36],
                            'tau_prime_7':new_population[:,37],
                            'beta_7':new_population[:,38],
                            'w_0_7':new_population[:,39],
                            'u_e_7':new_population[:,40],
                            'kf_7':new_population[:,41],
                            'tau_8':new_population[:,42],
                            'tau_prime_8':new_population[:,43],
                            'beta_8':new_population[:,44],
                            'w_0_8':new_population[:,45],
                            'u_e_8':new_population[:,46],
                            'kf_8':new_population[:,47],
                            'w_21':fixed_CPG_array[0],
                            'w_32':fixed_CPG_array[1],
                            'w_43':fixed_CPG_array[2],
                            'w_51':fixed_CPG_array[3],
                            'w_65':fixed_CPG_array[4],
                            'w_76':fixed_CPG_array[5],
                            'w_87':fixed_CPG_array[6],
                            'Fitness': fitness})
        log('[GA] {0}'.format(df.to_string()))
        #print(df)
        log('[GA] Generation{0}-Fitness{1}'.format(generation, fitness))
        file_name = 'Snake_Generation_' + str(generation)
        excel_logger(df, file_name) 
        # Selecting the best parents in the population for mating.
        parents = GA01.select_mating_pool(new_population, fitness, 
                                          NUM_PARENTS_MATING)
        #print('Generation {0} - Best Parents mating {1}'.format(generation, parents) )    
        # Generating next generation using crossover.
        offspring_crossover = GA01.crossover(parents,
                                           offspring_size=(pop_size[0]-parents.shape[0], FIRST_ITER_NUM_OF_PARAM))
        #print('fitness after crossover  ----------------------', fitness)
    
        # Adding some variations to the offsrping using mutation.
        offspring_mutation = GA01.mutation(offspring_crossover)
        
        #print('fitness after mutation----------------------', fitness)
    
        # Creating the new population based on the parents and offspring.
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation
        #print('fitness before best results ----------------------', fitness)
        # The best result in the current iteration.        
        #log("Best result : {0}".format(np.max(fitness)))
        #sys.exit()
        
    # Getting the best solution after iterating finishing all generations.
    #At first, the fitness is calculated for each solution in the final generation
    fitness = GA01.cal_pop_fitness(clientID, Handle, new_population, fixed_CPG_array)
    # Then return the index of that solution corresponding to the best fitness.
    best_match_idx = np.where(fitness == np.max(fitness))
    log("[GA] Best solution for  - tau, tau_prime, beta, w_0, u_e, kf,tau, tau_prime, beta, w_0, u_e, kf for all CPGs: {0} ".format(new_population[best_match_idx, :]))
    del fixed_CPG_array
    fixed_CPG_array1 = new_population[best_match_idx, :]  ## storing the values of optimised first iter CPG values and start optimizing rest
    ####deleting all arrays 
    del pop_size
    del new_population  
    del parents
    del offspring_crossover
    del offspring_mutation
    
    #######################################################################################################################
    ###################################  optimising - tau, tau_prime, beta, w_0, u_e, kf..... #############################
    #######################################################################################################################
    log('[GA] Creating position bounds for optimising - w_21, w_32, w_43....')
    log('[GA] Logging position bounds')
    log('[GA] MIN_w_21={0}, MAX_w_21={1}'.format(MIN_w_21, MAX_w_21))
    log('[GA] MIN_w_32={0}, MAX_w_32={1}'.format(MIN_w_32, MAX_w_32))
    log('[GA] MIN_w_43={0}, MAX_w_43={1}'.format(MIN_w_43, MAX_w_43))
    log('[GA] MIN_w_51={0}, MAX_w_51={1}'.format(MIN_w_51, MAX_w_51))
    log('[GA] MIN_w_65={0}, MAX_w_65={1}'.format(MIN_w_65, MAX_w_65))
    log('[GA] MIN_w_76={0}, MAX_w_76={1}'.format(MIN_w_76, MAX_w_76))
    log('[GA] MIN_w_87={0}, MAX_w_87={1}'.format(MIN_w_87, MAX_w_87))
    # Defining the population size.
    pop_size = (SOL_PER_POP,(TOT_NUM_OF_PARAM - FIRST_ITER_NUM_OF_PARAM))
    #Creating the initial population.
    new_population = [[0 for x in range(TOT_NUM_OF_PARAM - FIRST_ITER_NUM_OF_PARAM)] for y in range(SOL_PER_POP)] 
    for i in range(pop_size[0]):         
            new_population[i][0] = round(np.random.uniform(low=MIN_w_21, high=MAX_w_21), 2)
            new_population[i][1] = round(np.random.uniform(low=MIN_w_32, high=MAX_w_32), 2)
            new_population[i][2] = round(np.random.uniform(low=MIN_w_43, high=MAX_w_43), 2)            
            new_population[i][3] = round(np.random.uniform(low=MIN_w_51, high=MAX_w_51), 2)
            new_population[i][4] = round(np.random.uniform(low=MIN_w_65, high=MAX_w_65), 2)
            new_population[i][5] = round(np.random.uniform(low=MIN_w_76, high=MAX_w_76), 2)
            new_population[i][6] = round(np.random.uniform(low=MIN_w_87, high=MAX_w_87), 2) 
    new_population = np.array(new_population)
    log('[GA] Starting genetic algorithm for optimising - w_21, w_32, w_43, w_51.....')
    generation = 0
    for generation in range(FIRST_ITER_GEN,  NUM_OF_GEN):
        log('[GA] Running generation {0}'.format(generation))
        fitness = GA01.cal_pop_fitness(clientID, Handle,  new_population, fixed_CPG_array1)
        ## Saving logs in excel file 
        df = pd.DataFrame({ 'Chromosome ID' : [(i+1) for i in range(new_population.shape[0])],
                            'tau_1':fixed_CPG_array1[0][0][0],
                            'tau_prime_1':fixed_CPG_array1[0][0][1],
                            'beta_1':fixed_CPG_array1[0][0][2],
                            'w_0_1':fixed_CPG_array1[0][0][3],
                            'u_e_1':fixed_CPG_array1[0][0][4],
                            'kf_1':fixed_CPG_array1[0][0][5],
                            'tau_2':fixed_CPG_array1[0][0][6],
                            'tau_prime_2':fixed_CPG_array1[0][0][7],
                            'beta_2':fixed_CPG_array1[0][0][8],
                            'w_0_2':fixed_CPG_array1[0][0][9],
                            'u_e_2':fixed_CPG_array1[0][0][10],
                            'kf_2':fixed_CPG_array1[0][0][11],
                            'tau_3':fixed_CPG_array1[0][0][12],
                            'tau_prime_3':fixed_CPG_array1[0][0][13],
                            'beta_3':fixed_CPG_array1[0][0][14],
                            'w_0_3':fixed_CPG_array1[0][0][15],
                            'u_e_3':fixed_CPG_array1[0][0][16],
                            'kf_3':fixed_CPG_array1[0][0][17],
                            'tau_4':fixed_CPG_array1[0][0][18],
                            'tau_prime_4':fixed_CPG_array1[0][0][19],
                            'beta_4':fixed_CPG_array1[0][0][20],
                            'w_0_4':fixed_CPG_array1[0][0][21],
                            'u_e_4':fixed_CPG_array1[0][0][22],
                            'kf_4':fixed_CPG_array1[0][0][23],
                            
                            'tau_5':fixed_CPG_array1[0][0][24],
                            'tau_prime_5':fixed_CPG_array1[0][0][25],
                            'beta_5':fixed_CPG_array1[0][0][26],
                            'w_0_5':fixed_CPG_array1[0][0][27],
                            'u_e_5':fixed_CPG_array1[0][0][28],
                            'kf_5':fixed_CPG_array1[0][0][29],
                            'tau_6':fixed_CPG_array1[0][0][30],
                            'tau_prime_6':fixed_CPG_array1[0][0][31],
                            'beta_6':fixed_CPG_array1[0][0][32],
                            'w_0_6':fixed_CPG_array1[0][0][33],
                            'u_e_6':fixed_CPG_array1[0][0][34],
                            'kf_6':fixed_CPG_array1[0][0][35],
                            'tau_7':fixed_CPG_array1[0][0][36],
                            'tau_prime_7':fixed_CPG_array1[0][0][37],
                            'beta_7':fixed_CPG_array1[0][0][38],
                            'w_0_7':fixed_CPG_array1[0][0][39],
                            'u_e_7':fixed_CPG_array1[0][0][40],
                            'kf_7':fixed_CPG_array1[0][0][41],
                            'tau_8':fixed_CPG_array1[0][0][42],
                            'tau_prime_8':fixed_CPG_array1[0][0][43],
                            'beta_8':fixed_CPG_array1[0][0][44],
                            'w_0_8':fixed_CPG_array1[0][0][45],
                            'u_e_8':fixed_CPG_array1[0][0][46],
                            'kf_8':fixed_CPG_array1[0][0][47],
                            'w_21':new_population[:,0],
                            'w_32':new_population[:,1],
                            'w_43':new_population[:,2],
                            'w_51':new_population[:,3],
                            'w_65':new_population[:,4],
                            'w_76':new_population[:,5],
                            'w_87':new_population[:,6],
                            'Fitness': fitness})
        log('[GA] {0}'.format(df.to_string()))
        log('[GA] Generation{0}-Fitness{1}'.format(generation, fitness))
        file_name = 'Snake_Generation_' + str(generation)
        excel_logger(df, file_name) 
        parents = GA01.select_mating_pool(new_population, fitness, 
                                              NUM_PARENTS_MATING)
        offspring_crossover = GA01.crossover(parents,
                                               offspring_size=(pop_size[0]-parents.shape[0], TOT_NUM_OF_PARAM - FIRST_ITER_NUM_OF_PARAM))
        offspring_mutation = GA01.mutation(offspring_crossover)
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation
    fitness = GA01.cal_pop_fitness(clientID, Handle, new_population, fixed_CPG_array1)
    best_match_idx = np.where(fitness == np.max(fitness))
    log("[GA] Best solution after optimising all parameters of CPG: {0} ".format(new_population[best_match_idx, :]))   
        
    #log("[GA] Best solution fitness : {0}".format(fitness[best_match_idx]))
    #print("Best solution fitness : ", fitness[best_match_idx])
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
     ## Plot fitness 
#%%
elif (mode == 2):
    vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
    vrep.simxSynchronousTrigger(clientID) 
    VREP_com.vrep_reset_robot_joints(clientID, Handle)
    vrep.simxSynchronousTrigger(clientID) 
    vrep.simxGetPingTime(clientID)
    ## Run simple CPG based on provided values
    para1 = [0.35,1.71,4.689944495,1.03,2.12,0.23]
    para2 = [-0.84,-1.35,-0.88]
    osc1_out_val, osc2_out_val, osc3_out_val, osc4_out_val = CPG_osc.CPG_network(para1, para2)
    #print(osc1_out_val, osc2_out_val, osc3_out_val, osc4_out_val )
    
    for i in range(len(osc1_out_val)):
        OSC_Outputs = []
        
        OSC_Outputs.append(osc1_out_val[i])
        OSC_Outputs.append(osc2_out_val[i])
        OSC_Outputs.append(osc3_out_val[i])
        OSC_Outputs.append(osc4_out_val[i])
        
        #print(OSC_Outputs)
        
        VREP_com.vrep_moves_robot(clientID, Handle, np.array(OSC_Outputs))
        vrep.simxSynchronousTrigger(clientID) 
        vrep.simxGetPingTime(clientID)
        
        del OSC_Outputs
        VREP_com.vrep_get_inputs(clientID, Handle)
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
#%% 
else:
    print("You entered wrong mode... ")
    fitness_from_excel = []
    for i in range(40):
        file_mame = './Excel_files/Snake_Generation_' + str(i) + '.xlsx'
        df = pd.read_excel(file_mame)
        #print (df)
        fitness_from_excel.append(max(df['Fitness']))
    print(fitness_from_excel)
    file_name1 = 'fitness.xlsx'
    df1 = pd.DataFrame({'Fitness: ': fitness_from_excel})
    print(df1)
    writer = pd.ExcelWriter(file_name1)
    df1.to_excel(writer)
    writer.save()
    plt.figure() 
    plt.title('Fitness Graph')
    plt.ylabel('fitnewss (distance)')
    plt.xlabel('Num. of generation')
    plt.plot(np.arange(0,40), fitness_from_excel) 
    plt.grid()
    plt.legend()
    plt.savefig('./Graphs/Fitness_60_degree')    
    plt.show()
    del fitness_from_excel

