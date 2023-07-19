# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 08:24:27 2023

@author: skyet
"""

#References: https://www.osti.gov/servlets/purl/4609704
#https://app.knovel.com/hotlink/itble/rcid:kpMMDS0002/id:kt012J4NH2/matweb-metal-material/table-2-material-properties
#Kim, C S. Thermophysical properties of stainless steels. United States: N. p., 1975. Web. doi:10.2172/4152287.
#
Kanth_AMPT={
    "kclad": 22.2, #Thermal Conductivity averaged between 50C and 1200 C (W/m-k)
    "Tmelt": 1500.00, #melting Tempurature-C
    }

Zirc_2={
    "kclad": 17.9325, #Thermal Conductivity average between 100C and 800C (W/m-k)
    "Tmelt":1850.00, #melting Tempurature- C 
    }

Stain_Steel_304={
    "kclad": 19.5, # Thermal Conductivity average between 100C and 600C (W/m-K)
    "Tmelt": 1400-1450, #melting Tempurature-C
    }

Zirc_2_Nickel_Free={
    "kclad":18.1725, #Thermal Conductivity average between 100C and 800C (W/m-k) 
    }
    
Fuel_props = {
	"Kanth_AMPT": Kanth_AMPT,
	"Zirc_2": Zirc_2,
	"Stain_Steel_304": Stain_Steel_304,
	"Zirc_2_Nickel_Free": Zirc_2_Nickel_Free,
}