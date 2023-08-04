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
    "kclad": 22.2, #Thermal Conductivity averaged between 50C and 1200 C (323.15 K and 1473.15 K) (W/m-k)
    "Tmelt": 1500.00, #melting Tempurature-C
    "Tmelt_K": 1773.15, #melting Tempurature-K
    }

Zirc_2={
    "kclad": 19.02, #Thermal Conductivity average between 50C and 1000C (323.15 K and 1273.15K)  (W/m-k)
    "Tmelt":1850.00, #melting Tempurature- C 
    "Tmelt_K":2123.15, #melting Tempurature-K

    }


Stain_Steel_304={
    "kclad":21.83583333, # Thermal Conductivity average between 26.85C and 1026.85 C (300K and 1300 K) (W/m-K) 
    "Tmelt": 1400-1450, #melting Tempurature-C
    "Tmelt_K": 1673.15-1728.15, #melting tempurature-K
    }

Stain_Steel_304L={
    "kclad":21.83583333, # Thermal Conductivity average between 26.85C and 1026.85C (300k and 1300K)) (W/m-K)
    "Tmelt": 1400-1450, #melting Tempurature-C
    "Tmelt_K": 1673.15-1728.15, #melting tempurature-K
    }

Stain_Steel_316={
    "kclad":21.83583333, # Thermal Conductivity average between 100C and 600C (W/m-K)
    "Tmelt": 1400-1450, #melting Tempurature-C
    "Tmelt_K": 1673.15-1728.15, #melting tempurature-K
    }

Zirc_2_Nickel_Free={
    "kclad":18.1725, #Thermal Conductivity average between 100C and 800C (W/m-k) 
    }

Graphite_384_1={
        "kclad":90.016, #Thermal Conductivity average between 101 C and 1000.9 C (374.15 K and 1274.05 K)(W/m-K)
        "Tmelt":3600, #Melting Point-C
        "Tmelt_K": 3873.15, #Melting Point-K
    }

Graphite_384_2={
    "kclad":88.085, #Thermal Conductivity averaget between 101.1 C and 1000.7 C (398.58 K and 336.26K ) 
    "Tmelt": 3600, #Melting Point-C
    "Tmelt_K":3873.15, #Melting Point-K
    }

Fuel_props = {
	"Kanth_AMPT": Kanth_AMPT,
	"Zirc_2": Zirc_2,
	"Stain_Steel_304": Stain_Steel_304,
	"Zirc_2_Nickel_Free": Zirc_2_Nickel_Free,
}