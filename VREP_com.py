# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:46:23 2019

@author: MOC817
"""

import vrep
import sys
from math import pi
import numpy as np


tstep = 0.005
#%%
def vrep_connect():
    print ('Program started')
    vrep.simxFinish(-1)  
    clientID=vrep.simxStart('127.0.0.1',19998,True,True,5000,5) 
    
    if clientID!=-1:
        print ("Connected to remote API server")
        vrep.simxSetFloatingParameter(clientID, vrep.sim_floatparam_simulation_time_step, tstep, vrep.simx_opmode_oneshot)
        vrep.simxSynchronous(clientID, True)
    else:
        print("Not connected to remote API server")
        sys.exit("Could not connect")   
    return clientID

#%%
def vrep_robot_handle(clientID):
    
    Handle = np.zeros((1, 10))
    err_code, Handle[0, 0] = vrep.simxGetObjectHandle(clientID, "snake_joint_cam", vrep.simx_opmode_blocking)
    err_code, Handle[0, 1] = vrep.simxGetObjectHandle(clientID, "snake_joint_v1", vrep.simx_opmode_blocking)
    err_code, Handle[0, 2] = vrep.simxGetObjectHandle(clientID, "snake_joint_h1", vrep.simx_opmode_blocking)
    err_code, Handle[0, 3] = vrep.simxGetObjectHandle(clientID, "snake_joint_v2", vrep.simx_opmode_blocking)
    err_code, Handle[0, 4] = vrep.simxGetObjectHandle(clientID, "snake_joint_h2", vrep.simx_opmode_blocking)
    err_code, Handle[0, 5] = vrep.simxGetObjectHandle(clientID, "snake_joint_v3", vrep.simx_opmode_blocking)
    err_code, Handle[0, 6] = vrep.simxGetObjectHandle(clientID, "snake_joint_h3", vrep.simx_opmode_blocking)
    err_code, Handle[0, 7] = vrep.simxGetObjectHandle(clientID, "snake_joint_v4", vrep.simx_opmode_blocking)
    err_code, Handle[0, 8] = vrep.simxGetObjectHandle(clientID, "snake_joint_h4", vrep.simx_opmode_blocking)
    
    err_code, Handle[0, 9] = vrep.simxGetObjectHandle(clientID, "snake", vrep.simx_opmode_blocking)
    
    return Handle

#%%
clientID = vrep_connect()
Handle = vrep_robot_handle(clientID)
Handle = Handle.astype(int)

#%% 
def vrep_sim_check(clientID):
    while True: 
        vrep.simxGetIntegerSignal(clientID, 'asdf', vrep.simx_opmode_blocking)
        e =  vrep.simxGetInMessageInfo(clientID, vrep.simx_headeroffset_server_state)
        
        not_stopped  = e[1] & 1
        
        if not not_stopped:
            break
        else:
            vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)

#%%           
def vrep_reset_robot_joints(clientID, Handle):
    vrep.simxPauseCommunication(clientID, True)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 0], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 1], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 2], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 3], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 4], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 5], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 6], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 7], 0, vrep.simx_opmode_streaming)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 8], 0, vrep.simx_opmode_streaming)
    vrep.simxPauseCommunication(clientID, False)

#%%    
def vrep_get_inputs(clientID, Handle):
    err_code, Vjoint1_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 1], vrep.simx_opmode_streaming)
    err_code, Vjoint2_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 3], vrep.simx_opmode_streaming)
    err_code, Vjoint3_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 5], vrep.simx_opmode_streaming)
    err_code, Vjoint4_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 7], vrep.simx_opmode_streaming)
    err_code, camjoint_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 0], vrep.simx_opmode_streaming)
    
    err_code, Vjoint1_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 2], vrep.simx_opmode_streaming)
    err_code, Vjoint2_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 4], vrep.simx_opmode_streaming)
    err_code, Vjoint3_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 6], vrep.simx_opmode_streaming)
    err_code, Vjoint4_inputs = vrep.simxGetJointPosition(clientID, Handle[0, 8], vrep.simx_opmode_streaming)
    #print(Vjoint1_inputs, Vjoint2_inputs, Vjoint3_inputs, Vjoint4_inputs, camjoint_inputs )    
  
#%%          
def vrep_moves_robot(clientID, Handle, Outputs):
    Outputs[0] = round(Outputs[0]*(pi/3), 2)
    Outputs[1] = round(Outputs[1]*(pi/3), 2)
    Outputs[2] = round(Outputs[2]*(pi/3), 2)
    Outputs[3] = round(Outputs[3]*(pi/3), 2)
    Outputs[4] = round(Outputs[4]*(pi/3), 2)
    Outputs[5] = round(Outputs[5]*(pi/3), 2)
    Outputs[6] = round(Outputs[6]*(pi/3), 2)
    Outputs[7] = round(Outputs[7]*(pi/3), 2)
    
    
    vrep.simxPauseCommunication(clientID, True)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 1], Outputs[0], vrep.simx_opmode_oneshot)    
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 3], Outputs[1], vrep.simx_opmode_oneshot)    
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 5], Outputs[2], vrep.simx_opmode_oneshot)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 7], Outputs[3], vrep.simx_opmode_oneshot)
    
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 2], Outputs[0], vrep.simx_opmode_oneshot)    
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 4], Outputs[1], vrep.simx_opmode_oneshot)    
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 6], Outputs[2], vrep.simx_opmode_oneshot)
    err_code = vrep.simxSetJointTargetPosition(clientID, Handle[0, 8], Outputs[3], vrep.simx_opmode_oneshot)
    vrep.simxPauseCommunication(clientID, False) 
    

            
        

