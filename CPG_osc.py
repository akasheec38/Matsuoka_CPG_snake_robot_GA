# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:06:44 2019

@author: MOC817
"""
################# networkl of diffrent CPGs########################
import time
import matplotlib.pyplot as plt
import numpy as np
import os
from constants import NUM_OF_GEN, SOL_PER_POP


#%%
m1 = 1.0
m2 = 1.0
a = 1.0

dt = 0.01

#%%
if not os.path.exists('Graphs'):
    os.mkdir('Graphs')
generation_num = 0
chromososme_num = 0


#%%   ## one Matsuoka CPG Oscillator 
def CPG(u1, u2, v1, v2, y1, y2, f1, f2, s1, s2, dt, tau, tau_prime, beta, w_0, u_e, kf):
        
    tau *= kf
    tau_prime *= kf  
    
    d_u1_dt = (-u1 - w_0*y2 -beta*v1 + u_e + f1 + a*s1)/tau
    d_v1_dt = (-v1 + y1)/tau_prime
    y1 = max([0.0, u1])

    d_u2_dt = (-u2 - w_0*y1 -beta*v2 + u_e + f2 + a*s2)/tau
    d_v2_dt = (-v2 + y2)/tau_prime
    y2 = max([0.0, u2])

    u1 += d_u1_dt * dt
    u2 += d_u2_dt * dt
    v1 += d_v1_dt * dt
    v2 += d_v2_dt * dt

    o = (-m1*y1 + m2*y2)

    return u1, u2, o
    
#%%
def CPG_network(CPG_Para_arr1, CPG_Para_arr2):
    ##CPG_Para_arr ::::::::: containing 6 * number of CPG  elelemnts --in 4 joints : 24 param
    ##CPG_weight_arr:::::::::: weights param for 4 joints 3 param
    # Variables
    global generation_num 
    global chromososme_num
    
    if len(CPG_Para_arr1) == 48:
        tau_1 = CPG_Para_arr1[0]
        tau_prime_1 = CPG_Para_arr1[1]
        beta_1 = CPG_Para_arr1[2]
        w_0_1 = CPG_Para_arr1[3]
        u_e_1 = CPG_Para_arr1[4]
        kf_1 = CPG_Para_arr1[5]  
        tau_2 = CPG_Para_arr1[6]
        tau_prime_2 = CPG_Para_arr1[7]
        beta_2 = CPG_Para_arr1[8]
        w_0_2 = CPG_Para_arr1[9]
        u_e_2 = CPG_Para_arr1[10]
        kf_2 = CPG_Para_arr1[11]
        tau_3 = CPG_Para_arr1[12]
        tau_prime_3 = CPG_Para_arr1[13]
        beta_3 = CPG_Para_arr1[14]
        w_0_3 = CPG_Para_arr1[15]
        u_e_3 = CPG_Para_arr1[16]
        kf_3 = CPG_Para_arr1[17]
        tau_4 = CPG_Para_arr1[18]
        tau_prime_4 = CPG_Para_arr1[19]
        beta_4 = CPG_Para_arr1[20]
        w_0_4 = CPG_Para_arr1[21]
        u_e_4 = CPG_Para_arr1[22]
        kf_4 = CPG_Para_arr1[23]
        
        tau_5 = CPG_Para_arr1[24]
        tau_prime_5 = CPG_Para_arr1[25]
        beta_5 = CPG_Para_arr1[26]
        w_0_5 = CPG_Para_arr1[27]
        u_e_5 = CPG_Para_arr1[28]
        kf_5 = CPG_Para_arr1[29]  
        tau_6 = CPG_Para_arr1[30]
        tau_prime_6 = CPG_Para_arr1[31]
        beta_6 = CPG_Para_arr1[32]
        w_0_6 = CPG_Para_arr1[33]
        u_e_6 = CPG_Para_arr1[34]
        kf_6 = CPG_Para_arr1[35]
        tau_7 = CPG_Para_arr1[36]
        tau_prime_7 = CPG_Para_arr1[37]
        beta_7 = CPG_Para_arr1[38]
        w_0_7 = CPG_Para_arr1[39]
        u_e_7 = CPG_Para_arr1[40]
        kf_7 = CPG_Para_arr1[41]
        tau_8 = CPG_Para_arr1[42]
        tau_prime_8 = CPG_Para_arr1[43]
        beta_8 = CPG_Para_arr1[44]
        w_0_8 = CPG_Para_arr1[45]
        u_e_8 = CPG_Para_arr1[46]
        kf_8 = CPG_Para_arr1[47]
        
        w_21 = CPG_Para_arr2[0]
        w_32 = CPG_Para_arr2[1]
        w_43 = CPG_Para_arr2[2]
        w_51 = CPG_Para_arr2[3]
        w_65 = CPG_Para_arr2[4]
        w_76 = CPG_Para_arr2[5]
        w_87 = CPG_Para_arr2[6]
    
    if len(CPG_Para_arr1) == 7:
        tau_1 = CPG_Para_arr2[0][0][0]
        tau_prime_1 = CPG_Para_arr2[0][0][1]
        beta_1 = CPG_Para_arr2[0][0][2]
        w_0_1 = CPG_Para_arr2[0][0][3]
        u_e_1 = CPG_Para_arr2[0][0][4]
        kf_1 = CPG_Para_arr2[0][0][5] 
        tau_2 = CPG_Para_arr2[0][0][6]
        tau_prime_2 = CPG_Para_arr2[0][0][7]
        beta_2 = CPG_Para_arr2[0][0][8]
        w_0_2 = CPG_Para_arr2[0][0][9]
        u_e_2 = CPG_Para_arr2[0][0][10]
        kf_2 = CPG_Para_arr2[0][0][11] 
        tau_3 = CPG_Para_arr2[0][0][12]
        tau_prime_3 = CPG_Para_arr2[0][0][13]
        beta_3 = CPG_Para_arr2[0][0][14]
        w_0_3 = CPG_Para_arr2[0][0][15]
        u_e_3 = CPG_Para_arr2[0][0][16]
        kf_3 = CPG_Para_arr2[0][0][17] 
        tau_4 = CPG_Para_arr2[0][0][18]
        tau_prime_4 = CPG_Para_arr2[0][0][19]
        beta_4 = CPG_Para_arr2[0][0][20]
        w_0_4 = CPG_Para_arr2[0][0][21]
        u_e_4 = CPG_Para_arr2[0][0][22]
        kf_4 = CPG_Para_arr2[0][0][23] 
        
        tau_5 = CPG_Para_arr2[0][0][24]
        tau_prime_5 = CPG_Para_arr2[0][0][25]
        beta_5 = CPG_Para_arr2[0][0][26]
        w_0_5 = CPG_Para_arr2[0][0][27]
        u_e_5 = CPG_Para_arr2[0][0][28]
        kf_5 = CPG_Para_arr2[0][0][29] 
        tau_6 = CPG_Para_arr2[0][0][30]
        tau_prime_6 = CPG_Para_arr2[0][0][31]
        beta_6 = CPG_Para_arr2[0][0][32]
        w_0_6 = CPG_Para_arr2[0][0][33]
        u_e_6 = CPG_Para_arr2[0][0][34]
        kf_6 = CPG_Para_arr2[0][0][35] 
        tau_7 = CPG_Para_arr2[0][0][36]
        tau_prime_7 = CPG_Para_arr2[0][0][37]
        beta_7 = CPG_Para_arr2[0][0][38]
        w_0_7 = CPG_Para_arr2[0][0][39]
        u_e_7 = CPG_Para_arr2[0][0][40]
        kf_7 = CPG_Para_arr2[0][0][41] 
        tau_8 = CPG_Para_arr2[0][0][42]
        tau_prime_8 = CPG_Para_arr2[0][0][43]
        beta_8 = CPG_Para_arr2[0][0][44]
        w_0_8 = CPG_Para_arr2[0][0][45]
        u_e_8 = CPG_Para_arr2[0][0][46]
        kf_8 = CPG_Para_arr2[0][0][47] 
        
        w_21 = CPG_Para_arr1[0]
        w_32 = CPG_Para_arr1[1]
        w_43 = CPG_Para_arr1[2]
        w_51 = CPG_Para_arr1[3]
        w_65 = CPG_Para_arr1[4]
        w_76 = CPG_Para_arr1[5]
        w_87 = CPG_Para_arr1[6]
    u1_1,  u2_1,  v1_1,  v2_1,  y1_1,  y2_1,  o_1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_2,  u2_2,  v1_2,  v2_2,  y1_2,  y2_2,  o_2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_3,  u2_3,  v1_3,  v2_3,  y1_3,  y2_3,  o_3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_4,  u2_4,  v1_4,  v2_4,  y1_4,  y2_4,  o_4 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    
    u1_5,  u2_5,  v1_5,  v2_5,  y1_5,  y2_5,  o_5 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_6,  u2_6,  v1_6,  v2_6,  y1_6,  y2_6,  o_6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_7,  u2_7,  v1_7,  v2_7,  y1_7,  y2_7,  o_7 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    u1_8,  u2_8,  v1_8,  v2_8,  y1_8,  y2_8,  o_8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    o1_list = []
    o2_list = []
    o3_list = []
    o4_list = [] 
    
    #horigontal
    o5_list = []
    o6_list = []
    o7_list = []
    o8_list = [] 
    t_list = []

 
    for t in np.arange(0.0,20.0, dt):
        ##$ OSC for 4 virticle joint 
        #first vertical joint  osciltor 1 (pacemaker)
        f1_1, f2_1 = 0.0, 0.0
        s1_1, s2_1 = 0.0, 0.0
        u1_1, u2_1, o_1 = CPG(u1_1,u2_1, v1_1, v2_1, y1_1, y2_1, f1_1, f2_1, s1_1, s2_1, dt, 
                              tau_1, tau_prime_1, beta_1, w_0_1, u_e_1, kf_1)
        
        #vertical joint-2 (oscilator 2) 
        # vertical joint-1 master  (j =1), fisrt vertical joint slave (i = 2)
        #w_21 = -1.0
        f1_2, f2_2 = 0.0, 0.0
        s1_2, s2_2 = w_21*u1_1, w_21*u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_2, u2_2,  o_2 = CPG(u1_2, u2_2, v1_2, v2_2, y1_2, y2_2, f1_2, f2_2, s1_2, s2_2, dt,
                               tau_2, tau_prime_2, beta_2, w_0_2, u_e_2, kf_2)
        
        #vertical joint-3 (oscilator 3) 
        #vertical joint-2 (j =2), first horigontal joint slave (i = 3)
        #w_32 = -1.0
        f1_3, f2_3 = 0.0, 0.0
        s1_3, s2_3 = w_32*u1_1, w_32*u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_3, u2_3,  o_3 = CPG(u1_3, u2_3, v1_3, v2_3, y1_3, y2_3, f1_3, f2_3, s1_3, s2_3, dt,
                               tau_3, tau_prime_3, beta_3, w_0_3, u_e_3, kf_3)

        #vertical joint-4 (oscilator 4 ) 
        # vertical joint 3 master (j =3),  vertical joint 2  joint slave (i = 4)
        #w_43 = -1.0
        f1_4, f2_4 = 0.0, 0.0
        s1_4, s2_4 = w_43*u1_2, w_43*u2_2  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_4, u2_4,  o_4 = CPG(u1_4, u2_4, v1_4, v2_4, y1_4, y2_4,f1_4, f2_4, s1_4, s2_4, dt,
                               tau_4, tau_prime_4, beta_4, w_0_4, u_e_4, kf_4)
        
        #first horigontal joint  osciltor 1 
        # vertical joint-1 master  (j =1), fisrt horigontal joint slave (i = 5)
        #w_51 = 1.0
        f1_5, f2_5 = 0.0, 0.0
        s1_5, s2_5 =  w_51*u1_1,  w_51*u2_1 
        u1_5, u2_5, o_5 = CPG(u1_5, u2_5, v1_5, v2_5, y1_5, y2_5,f1_5, f2_5, s1_5, s2_5,dt, 
                              tau_5, tau_prime_5, beta_5, w_0_5, u_e_5, kf_5)
        
         #Horigontal joint-2 (oscilator 2) 
        # horigontal joint-1 master  (j =5), horigontal joint 2 slave (i = 6)
        #w_65 = -1.0
        f1_6, f2_6 = 0.0, 0.0
        s1_6, s2_6 = w_65*u1_5, w_65*u2_5  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_6, u2_6,  o_6 = CPG(u1_6, u2_6, v1_6, v2_6, y1_6, y2_6,f1_6, f2_6, s1_6, s2_6,dt,
                               tau_6, tau_prime_6, beta_6, w_0_6, u_e_6, kf_6)
        
        #horigontal joint-3 (oscilator 3) 
        #horigontal joint-2 (j =6),  horigontal joint 3 slave (i = 7)
        #w_76 = -1.0
        f1_7, f2_7 = 0.0, 0.0
        s1_7, s2_7 = w_76*u1_6, w_76*u2_6  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_7, u2_7, o_7 = CPG(u1_7, u2_7, v1_7,v2_7, y1_7, y2_7,f1_7, f2_7, s1_7, s2_7,dt, 
                              tau_7, tau_prime_7, beta_7, w_0_7, u_e_7, kf_7)
        
        #vertical joint-4 (oscilator 4 ) 
        # vertical joint 3 master (j =7),  vertical joint 2  joint slave (i = 8)
        #w_87 = -1.0
        f1_8, f2_8 = 0.0, 0.0
        s1_8, s2_8 = w_87*u1_7, w_87*u2_7  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
        u1_8, u2_8, o_8 = CPG(u1_8, u2_8, v1_8, v2_8, y1_8, y2_8,f1_8, f2_8, s1_8, s2_8,dt, 
                              tau_8, tau_prime_8, beta_8, w_0_8, u_e_8, kf_8)
        o1_list.append(o_1)
        o2_list.append(o_2)
        o3_list.append(o_3)
        o4_list.append(o_4)
        #horigontal
        o5_list.append(o_5)
        o6_list.append(o_6)
        o7_list.append(o_7)
        o8_list.append(o_8)
        t_list.append(t)  
        
    ##Normalise CPG Out values from -1.0 to 1.0 
    if (max(o1_list) > 1.0 or min(o1_list) < -1.0):
        o1_list =  [(float(i)-min(o1_list))/(max(o1_list)-min(o1_list)) for i in o1_list]
    if (max(o2_list) > 1.0 or min(o2_list) < -1.0):
        o2_list = [(float(i)-min(o2_list))/(max(o2_list)-min(o2_list)) for i in o2_list]
    if (max(o3_list) > 1.0 or min(o3_list) < -1.0):
        o3_list = [(float(i)-min(o3_list))/(max(o3_list)-min(o3_list)) for i in o3_list]
    if (max(o4_list) > 1.0 or min(o4_list) < -1.0):
        o4_list = [(float(i)-min(o4_list))/(max(o4_list)-min(o4_list)) for i in o4_list]
        
    if (max(o5_list) > 1.0 or min(o5_list) < -1.0):
        o5_list =  [(float(i)-min(o5_list))/(max(o5_list)-min(o5_list)) for i in o5_list]
    if (max(o6_list) > 1.0 or min(o6_list) < -1.0):
        o6_list = [(float(i)-min(o6_list))/(max(o6_list)-min(o6_list)) for i in o6_list]
    if (max(o7_list) > 1.0 or min(o7_list) < -1.0):
        o7_list = [(float(i)-min(o7_list))/(max(o7_list)-min(o7_list)) for i in o7_list]
    if (max(o8_list) > 1.0 or min(o8_list) < -1.0):
        o8_list = [(float(i)-min(o8_list))/(max(o8_list)-min(o8_list)) for i in o8_list]
        
    graph_name = './Graphs/Generation_'+ str(generation_num) + '_Chromosome_' + str(chromososme_num) + '_'+ str(time.strftime("%Y%m%d-%H%M%S"))
    chromososme_num += 1
    if chromososme_num == SOL_PER_POP:
        generation_num += 1
        chromososme_num = 0
        if generation_num == NUM_OF_GEN:
            generation_num = 0
            
    plt.figure() 
    plt.title('Generation_'+ str(generation_num) + '_Chromosome_' + str(chromososme_num))
    plt.ylabel('Normalised CPG Out value')
    plt.xlabel('time step')
    plt.plot(t_list, o1_list  , color='blue', label='joint_v1')
    plt.plot(t_list, o2_list  , color='black', label='joint_v2')
    plt.plot(t_list, o3_list  , color='purple', label='joint_v3')
    plt.plot(t_list, o4_list  , color='brown', label='joint_v4') 
    
    plt.plot(t_list, o5_list  , color='gray', label='horigontal_v1')
    plt.plot(t_list, o6_list  , color='pink', label='horigontal_v2')
    plt.plot(t_list, o7_list  , color='green', label='horigontal_v3')
    plt.plot(t_list, o8_list  , color='red', label='horigontal_v4')
    plt.grid()
    plt.legend()
    plt.savefig(graph_name)    
    plt.show()
    
    return o1_list, o2_list, o3_list, o4_list,  o5_list, o6_list, o7_list, o8_list

        
        
        
    
    
    
    
    
    
    
    
    
    
    
    