 # -*- coding: utf-8 -*-
"""
Created on Sun Dec. 10 10:57:35 2023

@author: skyet
"""
import LoadedTACO.src.HT9Props as clad
import LoadedTACO.src.HexDhCal as Geom
import LoadedTACO.src.HegNu as Nu
import LoadedTACO.src.TempBulkCal as TempBulk
import TACOCAT_Read_In_File as TCinput
import LoadedTACO.src.Geometry_Value as Geometry
from scipy.integrate import trapz
from scipy.integrate import quad
from LoadedTACO.src.Fuel_Props import Fuel_props
from LoadedTACO.src.Geometry_Value import Core_Geometry
from LoadedTACO.src.Coolant_Value import Coolant

#References: 
# 1.)https://www.sciencedirect.com/science/article/pii/S073519332030347X
#2.)https://www.thermal-engineering.org/what-is-dittus-boelter-equation-definition/
Uinlet = TCinput.Uinlet #average inlet velocity in a subchannel - m/s
Coolant_Type = TCinput.Coolant
Geometry_Type = TCinput.Geometry
Pr = Coolant[Coolant_Type]["Cp"]*Coolant[Coolant_Type]["nu"]*Coolant[Coolant_Type]["rho"]/Coolant[Coolant_Type]["k"] #Prandtl Number Calculation
Re = (Uinlet*Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"]/Coolant[Coolant_Type]["nu"])
b=0.4 #This is for heating. May need to revise in the future
f = 0.316*Re**(-0.25) #Re should be Re1. This is to test Nusselt Number Capabilities. Needs to be revised in the future
Dh=Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"]
L=Geometry.z
Prw=Pr #We assume that Prandlt Number at the wall is the same as the Prandlt number at the middle of the channel
# Defining Nusselt Number functions


def Nu_DB(Re,Pr,b):
    Nu=0.023*(Re**0.8)*(Pr**b)
    return Nu
    #Nu_DB (1,5,7)
    #print (Nu)


def Nu_Gn(f,Re,Pr,Dh,L,Prw):
    Nu=(((f/8)*(Re-1000)*Pr)/(1+12.7*((f/8)**(1/2))*((Pr**(2/3))-1)))*((1+((Dh/L)**(2/3)))*((Pr/Prw)**0.11))
    return Nu
   # Nu_Gn (9,11,13,15,17,19)
    #print (Nu)
# Preparing Functions for dictionary
Nu_dittus = Nu_DB(Re,Pr,b)
Nu_Gniel=Nu_Gn(f,Re,Pr,Dh,L,Prw)

Nus_DB={"NuCorrelation":Nu_dittus,}
Nus_Gn={"NuCorrelation":Nu_Gniel,}
#Dictionary
Nusselt={
    "DittusBoelter":Nus_DB,
    "Gnilenski":Nus_Gn,
}

