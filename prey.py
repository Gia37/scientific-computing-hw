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
l = range (101)

for i in range (101):
	y1 = D * Ky * Y0 - D * Kxy * x0 * y0 + y0
	x1 = D * Kyx * y0 * x0 - D * Kx * k0 + x0
	y0 = y1
	x0 = x1
	t [i] = y1

tnew = numpy.array (t)
lnew = numpy.array (l)

print xnew
print ynew

matplotlib.pyplot.plot(tnew, lnew)
matplotlib.pyplot.show ()

