# -*- coding: utf-8 -*-
"""
Created on Sun Dec. 10 10:57:35 2023

@author: skyet
"""

#References: 
# 1.)https://www.sciencedirect.com/science/article/pii/S073519332030347X
#2.)https://www.thermal-engineering.org/what-is-dittus-boelter-equation-definition/
# Defining Nusselt Number functions
def Nu_DB(Re,Pr,b):
    Nu=0.023*(Re**0.8)*(Pr**b)
    return Nu
    #Nu_DB (1,5,7)
    #print (Nu)


def Nu_Gn(f,Re,Pr,Dh,L,Prw):
    Nu=(((f/8)*(Re-1000)*Pr)/(1+12.7((f/8)**(1/2)))((Pr**(2/3))-1))*((1+((Dh/L)**(2/3)))((Pr/Prw)**0.11))
    return Nu
   # Nu_Gn (9,11,13,15,17,19)
    #print (Nu)
# Preparing Functions for dictionary
Nus_DB=Nu_DB(Re,Pr,b)
Nus_Gn=Nu_Gn(f,Re,Pr,Dh,L,Prw)
#Dictionary
Nusselt={
    "DittusBoelter":Nus_DB,
    "Gnilenski":Nus_Gn,
}

