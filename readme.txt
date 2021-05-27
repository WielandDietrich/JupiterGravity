#### Readme.txt ######

online repository for the paper: "Linking Zonal Winds and Gravity II: explaining the equatorially antisymmetric gravity moments of Jupiter" 
by W. Dietrich, P. Wulff, J. Wicht and U.R. Christensen, accepted in MNRAS (2021)


The provided files contain data for the TC model (fig. 6, d). This is calculated using the interior model of Guillot (2003) shown in fig.2, 
and the antisymmetric mean flow (fig.3) modified by setting the flow outside TC to zero (according to eq.30 with \delta_\beta = 2^deg and 
\beta_{TC}  =20.9) with a hyperbolic tangent radial profile (eq. 34 with \delta_h = 500 and h=2975 km) 

- the three npy-files are formatted as python Numpy pickles and can be loaded and visualised with the Starbound_load.py routine. 

the three provided files contain three terms of fundamental DGL eq.(17) as densities (see eq.11) on a twodimensional (r, theta) grid 

- sourceterm.npy contains the source \rho^U calculated with eq.26
- density_anomaly.npy contains the anomalous density (rho^\prime in eq.11)  
- DSG.npy contains the DSG term \mu \Psi^\prime
