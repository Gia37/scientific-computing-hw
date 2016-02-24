#Codigo del dia Feb-23-2016
#Gisela Arrieta Rivera
#Definir dos funciones f() y g() para un nuevo mapa logistico

import numpy
import matplotlib 
import matplotlib.pyplot

def funciong (t, r):
	return -r*t

def funcionf (z, delta, r):
	return z + delta *funciong(z,r)

y0 = 0.1
delta = 0.01 
r = 2.0
u = funcionf (y0, delta, r)

print u

n = 100
t = range (n)
y = range (n)

for i in range(n):
	y1 = funcionf (y0, delta, r)
	y[i] = y1




### Hoy 24/Feb modificamos este archivo
