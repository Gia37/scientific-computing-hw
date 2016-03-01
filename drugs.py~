import numpy
import matplotlib
import matplotlib.pyplot

# Encontrar cual es la concentracion de aspirina despues de 10 horas
# Hacer grafico de Q(n)/t
# Metodo: 
# Fecha: 25/Feb/2016
# Autor: Gisela Arrieta Rivera

k = 0.2
Q0 = 200
D = 0.1
x = range (101)
y = range (101)


for i in range (101):
	Q1 = Q0 - k * D * Q0
	Q0 = Q1
	x[i] = Q1
	y[i] = 	(i * 0.1)

xnew = numpy.array (x)
ynew = numpy.array (y)

print xnew
print ynew

matplotlib.pyplot.plot(ynew, xnew)
matplotlib.pyplot.show ()



 

