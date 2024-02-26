# -*- coding: utf-8 -*-
"""
Created on Thursday February 22 2024

@author: benjamin.lamballais
"""


import os, sys, re, string
import numpy as np
import pylab

sys.path.append(r'c:/Program Files/Simcenter/2210/Amesim/sys/python/win64python')
import ame_apy
if 'ame_apy' not in sys.modules:
   try:
      from ame_apy import *
   except ImportError:
      print ('Unable to import AMESim API module.\nCheck the AME environment variable.')

#Start API session
ame_apy.AMEInitAPI()

#Load model
ame_apy.AMEOpenAmeFile("c:/Users/benjamin.lamballais/Documents/Amesim/Entrainement/Gaussin_refueling_model_vPy.ame")

#Modify a global parameter
ame_apy.AMESetGlobalParameterValue('HPL_Di','10')

#Run single simulation
ame_apy.AMERunSimulation()

#Retrieve and plot a variable
res= ame_apy.AMEGetVariableValues('mass flow rate ')
variable_title= ame_apy.AMEGetVariableInfos('mass flow rate ')
x = np.array(res)
pylab.plot(x[:,0], x[:,1])

#Save and close model
ame_apy.AMECloseCircuit(True)

#Terminate API Session
ame_apy.AMECloseAPI()
