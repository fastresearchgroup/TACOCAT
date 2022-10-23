#Trevor Franklin

import pytest
import numpy as np
import matplotlib.pyplot as plt 
#import os
#import sys
#sys.path.insert(0,'..') #This adds the ability to pull modules from the main folder
#from pathlib import Path
import TACOCAT
import LoadedTACO.src.Flux_Profiles as Flux_Profiles
import LoadedTACO.src.Geometry_Value as geometry
import TACOCAT_Read_In_File as TCinput 
from LoadedTACO.src.Geometry_Value import Core_Geometry
from LoadedTACO.src.Coolant_Value import Coolant

steps = geometry.steps
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)
Coolant_Type = TCinput.Coolant
Geometry_Type = TCinput.Geometry
qlin = TCinput.Qth/(geometry.NFuel*TCinput.Hc)

C = (geometry.NFuel*qlin)/(Coolant[Coolant_Type]["Cp"]*TCinput.Uinlet*Coolant[Coolant_Type]["rho"]*Core_Geometry[Geometry_Type]["CoolantFlowArea"])

TestingTB = np.zeros(steps)
TestingTB[:] = (1/2)*z[:]**2

TempBulk = TACOCAT.BulkTemp(Flux_Profiles.LinearFlux)

TestTB = np.zeros(steps)
TestTB[0] = TCinput.Tbulkin
for i in range(1,steps):
	TestTB[i] = C*TestingTB[i]+TCinput.Tbulkin

np.testing.assert_allclose(TestTB, TempBulk, rtol=10)

'''
plt.plot(z,TempBulk)
plt.plot(x,ROC_TestTB)
plt.show()
'''