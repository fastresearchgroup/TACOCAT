#Lane Caraik
#Last Modified: 12/15/2015



import numpy as np
import matplotlib as mpl

from ..calculations import HexDhCal
from scipy.integrate import trapz

Tbulk = np.array([1,0])



def Tbulk(z,FluxPro,Tbulkin,NFuel,qlin,Cp,Uinlet,rho,HaF):
	for i in range(2,8):
		Tbulk = Tbulkin + (np.array(trapz(z,None,i,0),FluxPro(np.array([0,i])))*NFuel*qlin)/(Cp*Uinlet*rho*HexDhCal.HaF(HexDhCal.Ha(Ac),NFuel,FoCD,WoD)) #Bulk Temperature of Coolant - C
		return Tbulk 

print(Tbulk)
