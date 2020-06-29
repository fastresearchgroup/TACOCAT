#Thermal physical properties for UPu-Zr10
#Reference: Manara, D., De Bruycker, F., Boboridis, K., Tougait, O., Eloirdi, R., & Malki, M. (2012). High temperature radiance spectroscopy measurements of solid and liquid uranium and plutonium carbides. Journal of Nuclear Materials, 1–3, 126–138.
			

import numpy as np 

def kfuel(T):
	kfuel = 23 #Thermal Conductivity of Fuel - W/m-K @ 1000 C
	return kfuel

Tmelt = 2506.85 #Melting temperature of UPu-Zr10 - C (2780 K)