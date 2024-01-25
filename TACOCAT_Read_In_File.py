#TACOCAT read in file

#Provide the name of the reactor
Reactor_Title = "Placeholder"
## Print Logicals for saving plots and data files 
# (0 - save, 1 or higher - do not save)
print_logic = 0
data_logic = 1

#Provide chemical composition of fuel. Fuel types include: U_Zr10, UC, UO2, PuO2, ThO2, UN, U3Si2, MOX, U
Fuel_Type = "U_Zr10"

#Provide chemical composition of coolant. Coolant types include: NaK, FLiBe, FLiNaK, NaF_ZrF4
Coolant = "NaK"

#Provide reactor geometry. Geometry types include: Hexagonal, Wire_Wrapped_Hexagonal, Square
Geometry = "Wire_Wrapped_Hexagonal"

#Provide flux profile. Flux profile includes: Flatline, Linear, Exponential, Chopped_Cosine
Flux = "Chopped_Cosine"

Hc = 0.35 #Active Height of Core is 2m
Qth = 3*10**6 #Core Thermal Production - W
#Mdot = #Total mass flow rate for the reactor. This will then be divided for subchannels.
Tbulkin = 550.00 #Bulk Temperature of NaK at the Inlet - C
HotF = 1.5 #Hottest Channel Factor Calculation
Uinlet = 0.0375 #average inlet velocity in a subchannel - m/s

'''
Example input:

#Provide chemical composition of fuel. Fuel types include: U_Zr10, UC, UO2, PuO2, ThO2, UN, U3Si2, MOX, U
Fuel_Type = "UC"

#Provide chemical composition of coolant. Coolant types include: NaK, FLiBe, FLiNaK, NaF_ZrF4
Coolant = "NaK"

#Provide reactor geometry. Geometry types include: Hexagonal, Wire_Wrapped_Hexagonal, Square
Geometry = "Wire_Wrapped_Hexagonal"

#Provide flux profile. Flux profile includes: Flatline, linear, exponential, cosine
Flux_Profile = "Cosine"

'''