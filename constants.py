# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:59:46 2019

@author: MOC817
"""

#%%
NUM_OF_OSC = 8
NUM_OF_CPG_PARAM  = 6
NUM_OF_CONNECT_WEIGHT = 7
TOT_NUM_OF_PARAM = (NUM_OF_OSC*NUM_OF_CPG_PARAM)+ NUM_OF_CONNECT_WEIGHT  ## Num of genes  6*4+3 = 27 --- ((CPG_Para*num_of_CPG) + num_of_connection_weight)
FIRST_ITER_NUM_OF_PARAM =  48  ## number of parameters need to be change in first iteration  (CPG_Para*num_of_CPG)  --assuming that we are fixing weight first
SOL_PER_POP = 90   ##Number of chromosome
 
NUM_OF_GEN = 40 ## Max number of generation to be run for terminating evalution process
FIRST_ITER_GEN = 22  ## how many geretaion wants to train foer first iteration
NUM_PARENTS_MATING = 70
 
#%%
MIN_tau, MAX_tau = 0.10, 1.35
MIN_tau_prime, MAX_tau_prime = 0.20, 2.70
MIN_beta, MAX_beta = 2.50, 3.80
MIN_w_0, MAX_w_0 = 0.10, 2.60
MIN_u_e, MAX_u_e = 0.50, 4.90
MIN_kf, MAX_kf = 0.20, 0.50

MIN_w_21, MAX_w_21 = -1.50, 1.50
MIN_w_32, MAX_w_32 = -1.50, 1.50
MIN_w_43, MAX_w_43 = -1.50, 1.50

MIN_w_51, MAX_w_51 = -1.50, 1.50
MIN_w_65, MAX_w_65 = -1.50, 1.50
MIN_w_76, MAX_w_76 = -1.50, 1.50
MIN_w_87, MAX_w_87 = -1.50, 1.50




