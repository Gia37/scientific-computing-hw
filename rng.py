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

# sum: basicamente suma todos los numeros que se encuentran en un arreglo

x = [1, 2, 3, 4, 5, 6]
y = sum(x)
print y 

# numpy.cumsum



#########
n = 200
np.random.normal(0.0, 10, n)

def brownian(n):
	
	for i in range(n):
		np.random.normal()



