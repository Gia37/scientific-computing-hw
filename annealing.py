# Autor: Gisela Arrieta Rivera
# Date: April 26 2016
# Problem 
#

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt


# 1. Crear una funcion llamada "cost" que devuelva el costo para una solucion dada lllamada "solution"
#### En este caso, el costo esta dado por la ecuacion 2: c(x) = e**(-(x - 1)**2)* sin(8x) + 1

n = 100

def cost(n):
	x = np.linspace(-3, 3, num = n)
	return (np.exp(-(x - 1)**2)* np.sin(8*x) + 1)

plt.plot (cost(n))
plt.show()

# 2. Hacer una grafica del costo de soluciones en el rango -3 o 3, e identifica un rango para el valor optimo.

x = np.linspace(-3, 3, num = n)
def cost(x):

	return (np.exp(-(x - 1)**2)* np.sin(8*x) + 1)

plt.plot (x, cost(x))
plt.show()


# 3. Crea una funcion que devuelva una nueva solucion dada una posible solucion dada 

