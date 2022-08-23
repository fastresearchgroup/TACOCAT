#Trevor Franklin
#Coolant Data

import numpy as np
import TACOCAT_Read_In_File as TCinput
import TACOCAT.src.NaK_Prop as NaK_Prop
import TACOCAT.src.NaF_ZrF4_Prop as NaF_ZrF4_Prop
import TACOCAT.src.FLiBe_Prop as FLiBe_Prop
import TACOCAT.src.FLiNaK_Prop as FLiNaK_Prop

steps = 36
Tbulkin = TCinput.Tbulkin
Tbulk = np.zeros(steps) #Initialize Bulk Temperature of Coolant - C
Tbulk[0] = Tbulkin
TbulkHotF = np.zeros(steps)
TbulkHotF[0] = Tbulkin

#-------------------------------------------------------------------------------------------------#
#Nak Properties
rhoNa = NaK_Prop.rhoNa(Tbulkin + 273.15)
rhoK = NaK_Prop.rhoK(Tbulkin + 273.15)
invrhoNaK = 0.22/rhoNa + 0.78/rhoK
rho_Nak = 1/invrhoNaK #kg/m^3
CpNa = NaK_Prop.CpNa(Tbulkin + 273.15)
CpK = NaK_Prop.CpK(Tbulkin + 273.15)
Cp_Nak = (10**3)*(0.22*CpNa + 0.78*CpK) #J/kg-K
k_Nak = NaK_Prop.k(Tbulkin + 273.15)
nu_Nak = NaK_Prop.nu(Tbulkin + 273.15)
TmeltCoolant_Nak = -12.6 #Melting Temperature of NaK - C
Tboil_Nak = 784.00 #Boiling Temperature of NaK - C
rhoNamax = NaK_Prop.rhoNa(Tbulk[steps-1] + 273.15)
rhoKmax = NaK_Prop.rhoK(Tbulk[steps-1] + 273.15)
CpNamax = NaK_Prop.CpNa(Tbulk[steps-1] + 273.15)
CpKmax = NaK_Prop.CpK(Tbulk[steps-1] + 273.15)
Cpmax_Nak = (10**3)*(0.22*CpNamax + 0.78*CpKmax) #J/kg-K
kmax_Nak = NaK_Prop.k(Tbulk[steps-1] + 273.15)
numax_Nak = NaK_Prop.nu(Tbulk[steps-1] + 273.15)
invrhoNaKmax = 0.22/rhoNamax + 0.78/rhoKmax
rhomax_Nak = 1/invrhoNaKmax #kg/m^3

#FLiBe Properties
rho_FliBe = FLiBe_Prop.rho(Tbulkin + 273.15)
Cp_FliBe = FLiBe_Prop.Cp(Tbulkin + 273.15)
k_FliBe = FLiBe_Prop.k(Tbulkin + 273.15)
nu_FliBe = FLiBe_Prop.nu(Tbulkin + 273.15)
TmeltCoolant_FliBe = 459 #Melting Temperature of FLiBe - C
Tboil_FliBe = 1430 #Boiling Temperature of FLiBe - C
rhomax_FliBe = FLiBe_Prop.rho(Tbulk[steps-1] + 273.15)
Cpmax_FliBe = FLiBe_Prop.Cp(Tbulk[steps-1] + 273.15)
kmax_FliBe = FLiBe_Prop.k(Tbulk[steps-1] + 273.15)
numax_FliBe = FLiBe_Prop.nu(Tbulk[steps-1] + 273.15)

#FLiNak Properties
rho_FLiNak = FLiNaK_Prop.rho(Tbulkin + 273.15)
Cp_FLiNak = FLiNaK_Prop.Cp(Tbulkin + 273.15)
k_FLiNak = FLiNaK_Prop.k(Tbulkin + 273.15)
nu_FLiNak = FLiNaK_Prop.nu(Tbulkin + 273.15)
TmeltCoolant_FLiNak = 454 #Melting Temperature of FLiNaK - C
Tboil_FLiNak = 1570 #Boiling Temperature of FLiNaK - C
rhomax_FLiNak = FLiNaK_Prop.rho(Tbulk[steps-1] + 273.15)
Cpmax_FLiNak = FLiNaK_Prop.Cp(Tbulk[steps-1] + 273.15)
kmax_FLiNak = FLiNaK_Prop.k(Tbulk[steps-1] + 273.15)
numax_FLiNak = FLiNaK_Prop.nu(Tbulk[steps-1] + 273.15)

#NaF_ZrF4 Properties
rho_NaF_ZrF4 = NaF_ZrF4_Prop.rho(Tbulkin + 273.15)
Cp_NaF_ZrF4 = NaF_ZrF4_Prop.Cp(Tbulkin + 273.15)
k_NaF_ZrF4 = NaF_ZrF4_Prop.k(Tbulkin + 273.15)
nu_NaF_ZrF4 = NaF_ZrF4_Prop.nu(Tbulkin + 273.15)
TmeltCoolant_NaF_ZrF4 = 500 #Melting Temperature of NaF_ZrF4 - C
Tboil_NaF_ZrF4 = 1350 #Boiling Temperature of NaF_ZrF4 - C
rhomax_NaF_ZrF4 = NaF_ZrF4_Prop.rho(Tbulk[steps-1] + 273.15)
Cpmax_NaF_ZrF4 = NaF_ZrF4_Prop.Cp(Tbulk[steps-1] + 273.15)
kmax_NaF_ZrF4 = NaF_ZrF4_Prop.k(Tbulk[steps-1] + 273.15)
numax_NaF_ZrF4 = NaF_ZrF4_Prop.nu(Tbulk[steps-1] + 273.15)

#-------------------------------------------------------------------------------------------------#
#Dictionaries

NaK = {
	"rhoNa" : rhoNa,
	"rhoK" : rhoK,
	"invrhoNaK" : invrhoNaK,
	"rho" : rho_Nak, 
	"CpNa" : CpNa,
	"CpK" : CpK,
	"Cp" : Cp_Nak, 
	"k" : k_Nak,
	"nu" : nu_Nak,
	"TmeltCoolant" : TmeltCoolant_Nak, 
	"Tboil" : Tboil_Nak, 
	"rhoNamax" : rhoNamax,
	"rhoKmax" : rhoKmax,
	"CpNamax" : CpNamax,
	"CpKmax" : CpKmax,
	"Cpmax" : Cpmax_Nak, 
	"kmax" : kmax_Nak,
	"numax" : numax_Nak,
	"invrhoNaKmax" : invrhoNaKmax,
	"rhomax" : rhomax_Nak, 
	}

FLiBe = {
	"rho" : rho_FliBe,
	"Cp" : Cp_FliBe,
	"k" : k_FliBe,
	"nu" : nu_FliBe,
	"TmeltCoolant" : TmeltCoolant_FliBe, 
	"Tboil" : Tboil_FliBe, 
	"rhomax" : rhomax_FliBe,
	"Cpmax" : Cpmax_FliBe,
	"kmax" : kmax_FliBe,
	"numax" : numax_FliBe,
	}

FLiNaK = {
	"rho" : rho_FLiNak,
	"Cp" : Cp_FLiNak,
	"k" : k_FLiNak,
	"nu" : nu_FLiNak,
	"TmeltCoolant" : TmeltCoolant_FLiNak, 
	"Tboil" : Tboil_FLiNak, 
	"rhomax" : rhomax_FLiNak,
	"Cpmax" : Cpmax_FLiNak,
	"kmax" : kmax_FLiNak,
	"numax" : numax_FLiNak,
	}

NaF_ZrF4 = {
	"rho" : rho_NaF_ZrF4,
	"Cp" : Cp_NaF_ZrF4,
	"k" : k_NaF_ZrF4,
	"nu" : nu_NaF_ZrF4,
	"TmeltCoolant" : TmeltCoolant_NaF_ZrF4, 
	"Tboil" : Tboil_NaF_ZrF4, 
	"rhomax" : rhomax_NaF_ZrF4,
	"Cpmax" : Cpmax_NaF_ZrF4,
	"kmax" : kmax_NaF_ZrF4,
	"numax" : numax_NaF_ZrF4,
	}
	
Coolant = {
	"NaK" : NaK,
	"FLiBe" : FLiBe, 
	"FLiNaK" : FLiNaK,
	"NaF_ZrF4" : NaF_ZrF4,
	}	
	
