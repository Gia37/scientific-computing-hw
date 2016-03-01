#Autor: Gisela Arrieta Rivera
#Fecha: Mar-01-2016
#Objetivo:
#

import numpy
import matplotlib
import matplotlib.pyplot

D = 0.1
x0 = 15
y0 = 100
Ky = 2.0
Kyx = 0.01
Kx = 1.06
Kxy = 0.01
t = range (101) 
y = range (101)

for i in range (101):
	Y0 = D * Ky * Y0 - D * Kxy * x0 

