#Fuel properties for TACOCAT calculations
#References:
	#Fuel:
		#UC: Manara, D., De Bruycker, F., Boboridis, K., Tougait, O., Eloirdi, R., & Malki, M. (2012). High temperature radiance spectroscopy measurements of solid and liquid uranium and plutonium carbides. Journal of Nuclear Materials, 1–3, 126–138.
		#U-Zr10: L. B. CARASIK, P. O’NEAL, M. KENNINGTON, T. HUGHES, H. HONANG, N, GOTH, A 3 MW NaK Cooled Fast Reactor for Use as the First Lunar Base Fission Power Unit, Technical Report, 2015.
		#All others: Todreas, N., Kazimi, M. (2012). Nuclear Systems: Thermal Hydraulic Fundamentals.

U_Zr10 = {
	"kfuel": 22, #Thermal Conductivity of Fuel - W/m-C @ 1000 C
	"Tmelt": 1160.00 #Melting temperature - C
}

UC = {
	"kfuel": 23, #Thermal Conductivity of Fuel - W/m-C
	"Tmelt": 2506.85 #Melting temperature - C (2780 K)
}

UO2 = {
	"kfuel": 3.6, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2800 #Melting Temperature - C
}

PuO2 = {
	"kfuel": 4.3, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2374 #Melting Temperature - C
}

ThO2 = {
	"kfuel": 5.76, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 3378 #Melting Temperature - C
}

UN = {
	"kfuel": 21, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2800 #Melting Temperature - C
}

U3Si2 = {
	"kfuel": 15, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 1665 #Melting Temperature - C
}

MOX = {
	"kfuel": 3.7, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 2774 #Melting Temperature - C
	#MOX values are for 94% UO2 and 6% PuO2
}

U = {
	"kfuel": 32, #Thermal Conductivity of fuel averaged between 200 C and 1000 C - W/m-C
	"Tmelt": 1133 #Melting Temperature - C
}

Fuel_props = {
	"U_Zr10": U_Zr10,
	"UC": UC,
	"UO2": UO2,
	"PuO2": PuO2,
	"ThO2": ThO2,
	"UN": UN,
	"U3Si2": U3Si2,
	"MOX": MOX,
	"U": U
}