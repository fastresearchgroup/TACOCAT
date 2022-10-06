#Lane Caraik
#Last Modified: 12/15/2015

import numpy as np
import matplotlib as mpl
from LoadedTACO.src.Geometry_Value import Core_Geometry
from scipy.integrate import trapz
import os
import sys
sys.path.insert(0,'../..') #This adds the ability to geometry calculations from the main folder
import TACOCAT_Read_In_File as TCinput

Geometry_Type = TCinput.Geometry

Tbulk = np.array([1,0])

def Tbulk(z,FluxPro,Tbulkin,NFuel,qlin,Cp,Uinlet,rho):
	for i in range(2,8):
		Tbulk = Tbulkin + (np.array(trapz(z,None,i,0),FluxPro(np.array([0,i])))*NFuel*qlin)/(Cp*Uinlet*rho*Core_Geometry[Geometry_Type]["CoolantFlowArea"]) #Bulk Temperature of Coolant - C
		return Tbulk