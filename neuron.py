# Autor: Gisela Arrieta Rivera
# Fecha: 29-03-26

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math
from scipy.interpolate import interp1d

# Generates the data
x =np.linspace (0, 10, num=10, endpoint=True)
y = np.cos(-x**2 / 9.0)
f = interp1d(x, y, kind='cubic')

#Evaluates
print f(0.2)


T = 6.3
v = -65
delta = 0.001
phi = 3**(T-6.3)/10
alpha_n = phi * (0.01 * (v + 10)/(math.exp((v + 10)/10) -1))
alpha_m = phi * (0.01 * (v + 25)/(math.exp((v + 25)/10) -1))
alpha_h = phi * (0.07 * math.exp(V/20))
n0 = 0.317
m0 = 0.05
h0 = 0.6
beta_n = phi * (0.125 * math.exp(v/80))
beta_m = phi * (4 * math.exp(v/18))
beta_h = phi * (1/(math.exp((v + 30)/10) +1))
gk = 36
gNa = 120
gL = 0.3
vK = -77 
vL = -54.4
vNa = 50
I = 15
Ik = gk * n**4 * (v -vK)
Il = gL * (v - vL)
INa = gNa * m**3 * h * (v - vNa)
dn/dt = alpha_n * (1 - n0) - beta_n * n0
dm/dt = alpha_m * (1 - m0) - beta_m * m0
dh/dt = alpha_h * (1 - h) - beta_h * h


def f(u, t):			

	U = alpha_n * (1 - n0) - beta_n * n0
	t = 0.0003

	return U, t















def gn(an):
	if phi(0.01 * (V + 10)/(math.exp * ((V + 10)/10) -1)	
	return an

def gm(am):
	if phi(0.01 * (V + 25)/(math.exp * ((V + 25)/10) -1)
	return am

def gh(ah):
	if phi(0.07 * np.exp * (V/20))
	return ah
#########################################

for e in range (f(0), f(5))
	n1 = delta * (alpha_n * (1-n0)- beta_n0 * n0) + n0
	n0 = n1
print n1



for s in range (f(0), f(5)):
	m1 = delta * (alpha_m * (1-m0)- beta_m0 * m0) + m0
	m0 = m1
print m1


for p in range (f(0), f(5)):
	h1 = delta * (alpha_h * (1-h0)- beta_h0 * h0)
	h0 = h1
print m1




