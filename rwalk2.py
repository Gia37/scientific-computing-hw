
# Gisela Arrieta Rivera
# 

import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt


# s es un contador

def rwalk1d(N, p):
	s = 0
	for i in range(N):
		l = np.random.random()
		if l > p: 
			s = s + 1
		else:	
			s = s - 1
	return s

print 'la posicion final es: ', rwalk1d(1000, 0.2)





