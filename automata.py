# Autor: Gisela Arrieta Rivera
# Fecha: Mayo 3 2016
#

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

# P1 crear una cuadricula cuadrada de tamano n * n, con n = 100
i = 100
j = 100
x = range (i, j)
n = 100

def square(x): 
	for n in range(100):
		w = np.zeros([n, n], dtype = np.int8)
		

plt.plot(n, square(n))
plt.show()



# P2 

blanco = wh
negro = bl
direccion = d
color = c

def nextdirection (d, c):
	este = 0 # derecha
	sur = 1 # abajo
	oeste = 2 # izquierda
	norte = 3 # arriba
	return 


# P3

def moveforward (i, j, d):

# P4

def validindex (i, j, n)

# P5

i = n/2
j= n/2
d = 0
n = 20000

# P6 plot 
plt.imshow(w, interpolation = ´none´, cmap = plt.cm.Greys, extent = (0, n, 0, n))
