# Autor: Gisela Arrieta Rivera
# Fecha: 29-03-26

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
from scipy.interpolate import interpld

# Generates the data
x =np.linspace (0, 10, num=10, endpoint=True)
y = np.cos(-x**2 / 9.0)
f = interpld(x, y, kind='cubic')

#Evaluates
print f(0.2)


T = 6.3
V = -65
delta = 0.001
phi = 3**(T-6.3)/10
alpha_n = phi(0.01(V + 10)/(np.exp((V + 10)/10) -1)
alpha_m = phi(0.01(V + 25)/(np.exp((V + 25)/10) -1)
alpha_h = phi(0.07 np.exp(V/20))
n = 0.317
m = 0.05
h = 0.6
beta_n = phi(0.125 np.exp(V/80))
beta_m = phi(4 np.exp(V/18))
beta_h = phi(1/(np.exp((V + 30)/10) +1)

def alpha_n(phi, V):
	phi(0.07 np.exp(V/20))	
	return alpha_n






