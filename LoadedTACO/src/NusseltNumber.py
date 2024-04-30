 # -*- coding: utf-8 -*-
"""
Created on Sun Dec. 10 10:57:35 2023

@author: skyet
"""
def Nu_DB(Re,Pr,b):
    Nu=0.023*(Re**0.8)*(Pr**b)
    return Nu

def Nu_Gn(f,Re,Pr,Dh,L,Prw):
    Nu=(((f/8)*(Re-1000)*Pr)/(1+12.7*((f/8)**(1/2))*((Pr**(2/3))-1)))*((1+((Dh/L)**(2/3)))*((Pr/Prw)**0.11))
    return Nu

#Dictionary
Nusselt={
    "DittusBoelter":Nu_DB,
    "Gnilenski":Nu_Gn,
}


