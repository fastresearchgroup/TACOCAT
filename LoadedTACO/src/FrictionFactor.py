# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:35:44 2024

@author: skyet
"""


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

def Haaland (Re, roughness):
     f=0.3086/(((log(6.9/Re+roughness*D)^1.11))^2)
     return f

#Preparing Functions for dictionary
Friction_Factor={
     "Blasius":Blasius,
     "laminar":lam,
     "Haaland":Haaland,
}

