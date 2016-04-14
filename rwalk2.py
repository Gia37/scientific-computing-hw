
# Gisela Arrieta Rivera
# 14-04-16

import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt


# s es un contador

n = 100
N = 1000
p = 0.5
h = 2 * N + 1


def rwalk1d(N, p):
	s = 0
	for i in range(N):
		l = np.random.random()
		if l > p: 
			s = s + 1
		else:	
			s = s - 1
	return s

print 'la posicion final es: ', rwalk1d(1000, 0.5)

n = 100
N = 1000
p = 0.5

def g(N):
	c = 0	
	for i in range(n):
		if x = rwalk1d(N, p):
			c = c + 1
			return c

print x

	
	

