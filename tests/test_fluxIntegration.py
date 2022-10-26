#Trevor Franklin
#BulkTemp integration test for straight line

import pytest
from pytest import approx
import numpy as np
import matplotlib.pyplot as plt
import TACOCAT.TACOCAT as TC
import LoadedTACO.src.Flux_Profiles as Flux_Profiles
import LoadedTACO.src.Geometry_Value as geometry
import TACOCAT_Read_In_File as TCinput 
from LoadedTACO.src.Geometry_Value import Core_Geometry
from LoadedTACO.src.Coolant_Value import Coolant

#Defining Constants
steps = geometry.steps
Hc = TCinput.Hc
z = np.linspace(-Hc/2,Hc/2,steps)
Coolant_Type = TCinput.Coolant
Geometry_Type = TCinput.Geometry
qlin = TCinput.Qth/(geometry.NFuel*TCinput.Hc)

#Defining Integration Constant 
C = (geometry.NFuel*qlin)/(Coolant[Coolant_Type]["Cp"]*TCinput.Uinlet*Coolant[Coolant_Type]["rho"]*Core_Geometry[Geometry_Type]["CoolantFlowArea"])

#Plotting known integration for straight line
TestingTB = np.zeros(steps)
TestingTB[:] = (1/2)*z[:]**2

#Pulling BulkTemp plot from TACOCAT
TempBulk = TC.BulkTemp(Flux_Profiles.LinearFlux)

#Creating test bulk temp with known integration
TestTB = np.zeros(steps)
TestTB[0] = TCinput.Tbulkin
for i in range(1,steps):
	TestTB[i] = C*TestingTB[i]+TCinput.Tbulkin

#Testing that the arrays are equal with an absolute tolerence of 10 degrees celsius
def test_Temp_Bulk_Array():
	assert list(TempBulk)==approx(list(TestTB), abs=10)