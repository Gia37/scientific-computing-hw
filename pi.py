# Gisela Arrieta Rivera
# 

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

np.random.seed(0)

for j in range(7):	
	print np.random.random()
# Encontrar un numero aleatorio entre -1.5 y 1.5



R = 1
L = 3
N = 100
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

	gpi= ((L/R)**2) * (n/N)
	 
mifuncion (3, 1, 100)
 

	

