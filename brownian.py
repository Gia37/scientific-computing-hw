#Gisela Arrieta Rivera
# Abril 12 2016
#

import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt

# 1

def rwalk1d(N, p):
	s = 0
	for i in range(N):
	
		r = np.random.random()
		if r < p: # heads
			s = s + 1
		else:     # tails
			s = s - 1
	return s

# 2

m = 0
s = 0
n = 100
N = 1000
p = 0.3

for i in range(n):
	
	x = rwalk1d(N, p)
	m = m + x
	s = s + x**2

m = m / float(n)
s = s / float(n)
s = np.sqrt(s - m**2)

print m, s

print N * (2 * p - 1), np.sqrt(4 * N * p *(1 - p))

# 3

N = 1000
n = 1000
p = 0.7

x = np.arange(2 * N + 1) - N
h = np.zeros(2 * N + 1)

for i in range(n):
	xfinal = rwalk1d(N, p)
	h[xfinal + N] += 1

