import NaK_Prop
import FLiBe_Prop
import FLiNaK_Prop
import NaF_ZrF4_Prop
import TACOCAT_Read_In_File as TCinput

steps = TCinput.steps
Tbulkin = TCinput.Tbulkin #Bulk Temperature of NaK at the Inlet - C

NaK = {
	"rho": 1/((0.22/NaK_Prop.rhoNa(Tbulkin + 273.15))+(0.78/NaK_Prop.rhoK(Tbulkin + 273.15))), #kg/m^3
	"Cp": (10**3)*(0.22*NaK_Prop.CpNa(Tbulkin + 273.15) + 0.78*NaK_Prop.CpK(Tbulkin + 273.15)), #J/kg-K
	"k": NaK_Prop.k(Tbulkin + 273.15),
	"nu": NaK_Prop.nu(Tbulkin + 273.15),
	"TmeltCoolant": -12.6, #Melting Temperature of NaK - C
	"Tboil": 784.00 #Boiling Temperature of NaK - C
}

FLiBe = {
	"rho": FLiBe_Prop.rho(Tbulkin + 273.15),
	"Cp": FLiBe_Prop.Cp(Tbulkin + 273.15),
	"k": FLiBe_Prop.k(Tbulkin + 273.15),
	"nu": FLiBe_Prop.nu(Tbulkin + 273.15),
	"TmeltCoolant": 459, #Melting Temperature of FLiBe - C
	"Tboil": 1430 #Boiling Temperature of FLiBe - C
}

FLiNaK = {
	"rho": FLiNaK_Prop.rho(Tbulkin + 273.15),
	"Cp": FLiNaK_Prop.Cp(Tbulkin + 273.15),
	"k": FLiNaK_Prop.k(Tbulkin + 273.15),
	"nu": FLiNaK_Prop.nu(Tbulkin + 273.15),
	"TmeltCoolant": 454, #Melting Temperature of FLiNaK - C
	"Tboil": 1570 #Boiling Temperature of FLiNaK - C
}

NaF_ZrF4 = {
	"rho": NaF_ZrF4_Prop.rho(Tbulkin + 273.15),
	"Cp": NaF_ZrF4_Prop.Cp(Tbulkin + 273.15),
	"k": NaF_ZrF4_Prop.k(Tbulkin + 273.15),
	"nu": NaF_ZrF4_Prop.nu(Tbulkin + 273.15),
	"TmeltCoolant": 500, #Melting Temperature of NaF_ZrF4 - C
	"Tboil": 1350 #Boiling Temperature of NaF_ZrF4 - C
}

Coolant_props = {
	"NaK": NaK,
	"FLiBe": FLiBe,
	"FLiNaK": FLiNaK,
	"NaF_ZrF4": NaF_ZrF4
}