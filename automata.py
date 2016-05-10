# Autor: Gisela Arrieta Rivera
# Fecha: Mayo 3 2016
#

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

# P1 crear una cuadricula cuadrada de tamano n * n, con n = 100

n = 100

w = np.zeros([n, n], dtype = np.int8)
		

plt.plot()
plt.show()


# P2 

blanco = 0
negro = 1
Dir = d
Color = c

def nextdirection (d, c):
	este = 0 #derecha
	sur = 1 # abajo
	oeste = 2 # izquierda
	norte = 3 # arriba
	if c == blanco:
		if d == norte:
			df = este
		if d == este:
			df = sur
		if d ==  sur:
			df = oeste
		if d == oeste:
			df = norte
	else:
		if d == norte:
			df = oeste
		if d == Oeste:
			 df = sur
		if d == sur:
			df = este
		if d == este:
			df = norte

	return df
		

# P3

#mueva hacia adelante
def moveforward (i, j, d):
	M[i][j] = 1
	if df == norte
		M[i-1][j] = df
	if df == sur 
		M[i + 1][j] = df
	if df == oeste
		M[i][j + 1] = df
	if df == este
		M[i][j - 1] = df
	return M
	

# P4

	def validindex (i, j, n):

# P5
i = n/2
j= n/2
d = 0
n = 20000

for i in range (n):


# P6 plot 
plt.imshow(w, interpolation = ´none´, cmap = plt.cm.Greys, extent = (0, n, 0, n))



