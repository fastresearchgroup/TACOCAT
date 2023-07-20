# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:28:54 2023

@author: skyet
"""
import Clad_Props as Clinput
Cladding_Type = Clinput.Fuel_props 

kclad_AMPT = 22.2 
kclad_Zirc_2 = 17.9325 
kclad_Stain_Steel_304 = 19.5 
kclad_Zirc_2_Nickel_Free = 18.1725 

Tmelt_AMPT = 1500.00
Tmelt_Zirc_2 = 1850.00
Tmelt_Stain_Steel_304 = '1400-1450'

print('----------------------------------------------')
print('Kanth_AMPT:',Tmelt_AMPT, 'C', )
print('Zirc_2:' ,Tmelt_Zirc_2, 'C')
print('Stain_Steel_304:',Tmelt_Stain_Steel_304, 'C')
print('Zirc_2_Nickel_Free:', 'C')
print('-----------------------------------------------')

