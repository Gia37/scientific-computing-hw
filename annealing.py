# Autor: Gisela Arrieta Rivera
# Date: April 26 2016
# Problem 
#

import numpy as np
import matplotlib 
import matplotlib.pyplot as plt


# 1. Crear una funcion llamada "cost" que devuelva el costo para una solucion dada lllamada "solution"
#### En este caso, el costo esta dado por la ecuacion 2: c(x) = e**(-(x - 1)**2)* sin(8x) + 1

n = 100 # soluciones 

def cost(n):
	x = np.linspace(-3, 3, num = n)
	return np.exp(-(x - 1)**2)* np.sin(8*x) + 1

plt.plot (cost(n))
plt.show()

# 2. Hacer una grafica del costo de soluciones en el rango -3 o 3, e identifica un rango para el valor optimo.

x = np.linspace(-3, 3, num = n)
def cost(x):

	return np.exp(-(x - 1)**2)* np.sin(8*x) + 1

plt.plot (x, cost(x))
plt.show()


# 3. Crea una funcion que devuelva una nueva solucion dada una posible solucion dada 

def neighbor (solution):
	step_size = 1.0
	return (2* np.random.random()-1) *step_size + solution


# 4. comenzar con una solucion seleccionada al azar en el rango encontrado en el paso 2. Fijar T = 1 y Tmin = 10**-5

T = 1
Tmin = 10**-5.
n = 100

s = np.random.uniform(0, 2)
c = cost(s)

while T > Tmin:
	for i in range(100):
		s1 = neighbor(s)
		c1 = cost(s1)
		mu = np.random.random()
		if np.exp((c - c1)/ T > mu:
			s = s1
			c = c1
	T = fT * T
print ´La solucion optima: %f´ % (s)
print ´El costo de la solucion optima: %f´ % (c)

# 5. Generar una nueva solucion con la funcion neighbor

# 6. Decidir cual de las dos soluciones es la mejor basada en lo que comentamos anteriormente en la ecuacion 1: e**(c-c')/T>u

# 7. Repita los pasos 5 y 6 100 veces

# 8. Disminuye T por un factor de 0.9 y repita los pasos 5-7 hasta que la temperatura desciende por debajo de Tmin.


