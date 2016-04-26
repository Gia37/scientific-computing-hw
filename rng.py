#Gisela Arrieta Rivera
# Abril 19 2016
#

import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt

np.random.seed(0)

## Example

# draws n samples from different random distributions
n = 50000
xu = np.random.uniform(-20, 20, n)
xb = np.random.binomial(200, 0.25, n)
xn = np.random.normal(0.0, 10, n)

# generates the hostograms
bins = 30
y1, x1 = np.histogram(xu, bins = bins, density = True)
y2, x2 = np.histogram(xb, bins = bins, density = True)
y3, x3 = np.histogram(xn, bins = bins, density = True)

# shifts the edges
x1 = x1[0 : -1] + 0.5 * (x1[1] - x1[0])
x2 = x2[0 : -1] + 0.5 * (x2[1] - x2[0])
x3 = x3[0 : -1] + 0.5 * (x3[1] - x3[0])

# plot
plt.plot(x1, y1, 'b-')
plt.plot(x2, y2, 'r-')
plt.plot(x3, y3, 'g-')
plt.show()

# function sum and function numpy.cumsum

# 1 sum: basicamente suma todos los numeros que se encuentran en un arreglo, Cumsum devuelve el acumulado total hasta una posicion determinada de un arreglo.

x = [1, 2, 3, 4, 5, 6]
y = sum(x)
print y 

# 2 brownian random walk

np.random.seed(0)

def brownian(n):
	delta = np.random.normal(0, 1, n)
	x = np.append(0, np.cumsum)

	return x
x = brownian(200)
plt.plot(x)

# 3

N = 100
n = 200
s2 = np.zeros(n + 1)

for i in range (N):
	x = brownian(n)
	s2 = s2 + x**2

s2 /= float(N)
t = range(n + 1)

plt.plot(t, s2, 'r-')
plt.show()

# 4

slope, intercept, r_value, p_value, std_err = stats.linregress(t, s2)
print 'Coeficiente de difusion D = ', 0.5 * slope

