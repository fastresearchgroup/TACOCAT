Cladding Thermophysical Properties
===================================

Cladding materials are a material that covers the outer layer of a reactor. 
This prevents radioactive material from being discharged. 
There were several things that were collected when finding the information for the cladding materials. 
First, the Thermal Conductivity of each material was collected. 
These Thermal Conductivities were averaged between 100°C and 1000°C. 
Then the melting points were averaged. 
The melting temperatures were found in both Celsius and Kelvin.  

Thermal conductivity for different cladding materials. The provided melting temperatures were added in Kelvin below.
----------

Material                             Thermal Conductivity       Melting Temperature          References

Graphite-384_1                        90.016                    Not available                https://www.osti.gov/servlets/purl/4609704

Stainless Steel 304                   21.83583333               1673.15-1728.15 K            https://app.knovel.com/hotlink/itble/rcid:kpMMDS0002/id:kt012J4NH2/matweb-metal-material/table-2-material-properties

Stainless Steel 304L                  21.83583333               1673.15-1728.15 K            Kim, C S. Thermophysical properties of stainless steels. United States: N. p., 1975. Web. doi:10.2172/4152287.

Zircaloy-2                            19.02                     2123.15 K                    https://matweb.com/search/DataSheet.aspx?MatGUID=3f64b985402445c0a5af911135909344

Zircaloy-2 Nickel-Free                18.1725                   Not available      
             -- materials.sql
                      
The eight cladding props collected are listed above. 
The information gathered was found in academic articles and web pages. 
The information was put into Python and a Clad Props library was created. 
Afterward, the new cladding materials file was added to the existing TACOCAT Software.
The following two graphs show the difference between the Thermal Conductivities of Graphiet 384_1 and Zircaloy-2.
As seen when viewing both graphs, there is not much difference in the two graphs. 
This is due to the Thermal Conductivities being averaged.
It is assumed that if they are not averaged, a bigger difference would be seen when the graphs were compared.
![Alt Text](C:\Users\skyet\Documents\CladPropsRST\Figure 2023-09-26 153300-Graphite 381.png)

.. image::Figure2023-09-26153204-Zirc_2.png
C:\Users\skyet\Documents\CladPropsRST\Figure2023-09-26 153218-Zirc_2.png
(Graphs for Zircaloy-2)
C:\Users\skyet\Documents\CladPropsRST\Figure 2023-09-26 153237-Graphite 381.png
C:\Users\skyet\Documents\CladPropsRST\Figure 2023-09-26 153300-Graphite 381.png
(Graphs for Graphite 381_1)