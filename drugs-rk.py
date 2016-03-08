# Encontrar cual es la concentracion de aspirina despues de 10 horas: metodo de Euler
# Metodo: 
# Fecha: 08/03/2016
# Autor: Gisela Arrieta Rivera

import numpy
import matplotlib
import matplotlib.pyplot

k = 0.2
Q0 = 200
D = 0.1
x = range (101)
y = range (101)


def g(Q):
	return -k * Q 

for i in range (101):
	Q1 = Q0 + D * g(Q0 + 0.5 * D * g(Q0))
	Q0 = Q1
	x[i] = Q1
	y[i] = i * D

print Q1

xnew = numpy.array (x)
ynew = numpy.array (y)

print xnew
print ynew

matplotlib.pyplot.plot(ynew, xnew)
matplotlib.pyplot.show ()

