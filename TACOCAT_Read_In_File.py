#TACOCAT read in file

#Provide the name of the reactor
Reactor_Title = "Lunar_Reactor_689"

#Provide chemical composition of fuel. Fuel types include: U_Zr10, UC, UO2, PuO2, ThO2, UN, U3Si2, MOX, U
Fuel_Type = "UC"

#Provide chemical composition of coolant. Coolant types include: NaK, FLiBe, FLiNaK, NaF_ZrF4
Coolant = "NaK"

#Provide reactor geometry. Geometry types include: 
Geometry = ""

Hc = 0.35 #Active Height of Core is 2m
Qth = 3*10**6 #Core Thermal Production - W
#Mdot = #Total mass flow rate for the reactor. This will then be divided for subchannels.
Tbulkin = 550.00 #Bulk Temperature of NaK at the Inlet - C
HotF = 1.5 #Hottest Channel Factor Calculation
'''
Example input:

#Provide chemical composition of fuel. Fuel types include: U_Zr10, UC, UO2, PuO2, ThO2, UN, U3Si2, MOX, U
Fuel_Type = "UC"

#Provide chemical composition of coolant. Coolant types include: NaK, FLiBe, FLiNaK, NaF_ZrF4
Coolant = "NaK"

#Provide reactor geometry. Geometry types include: 
Geometry = ""

'''