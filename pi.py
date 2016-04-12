# Gisela Arrieta Rivera
# 

import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt


np.random.seed(0)

for j in range(7):	
	print np.random.random()
# Encontrar un numero aleatorio entre -1.5 y 1.5



R = 1
L = 3
N = 10000
y = 1.5-np.random.random() * 3


def pi(L, R, N):
	x = np.linspace(0,1, num=N, endpoint='true')
	n = 0
x=range(N)
y=range(N)
n = 0
for j in range(N):
	x[j] = L/2 -np.random.random() * 3
	y[j] = np.random.uniform(-1.5,1.5)
	
	if np.sqrt(x[j]**2) + (y[j]**2)<=R:
		n = n + 1

	gpi= (L/R)**2 * (n/float(N))
	 
print (np.pi, N, gpi)


# Definiendo la funcion rwalk1d
# p varia entre 0 y 100 porciento, entonces p va desde 0 hasta 1.0

def rwalk1d(N, p):
	s = 0
	for i in range(N):
		r = np.random.random()
		if r > p: 
			s = s + 1
		else:	
			s = s - 1
	return s






 


	

