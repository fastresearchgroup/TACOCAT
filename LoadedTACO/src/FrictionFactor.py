# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:35:44 2024

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
Re = (Uinlet*Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"]/Coolant[Coolant_Type]["nu"])
Dh=Core_Geometry[Geometry_Type]["InnerHydraulicDiameter"]
L=Geometry.z

def Blasius(Re,Geometry_Type):
    f = 0.316*Re**(-0.25)
    if Geometry_Type == "Wire_Wraped_Hexagonal":
         M=((1.034/(Geometry.PtoD**0.124))+(29.7*(Geometry.PtoD**6.94)*Re**0.086)/(Geom.LeadW(Geometry.FoCD,Geometry.WoD)/Geometry.FoCD)**2.239)**0.885 #modifier
    else:
         M=1.0
    return f

def lam(Re):
    f=64/Re
    return f
