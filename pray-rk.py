import numpy
import matplotlib
import matplotlib.pyplot


ky=2.0
kyx=0.01
kx=1.06
kxy=0.01
d=0.1
x0=15
y0=100
x=range(101)
y=range(101)
t=range(101)

def f(x):
	return   

for i in range(101):
	y1= d*ky*y0-d*kxy*x0*y0+y0
	y0=y1
	x1= d*kyx*y0*x0-d*kx*x0+x0  
	x0=x1
        x[i]=x1
	y[i]=y1
	t[i]=i*0.1
	

xnew=numpy.array(x)
ynew=numpy.array(y)
tnew=numpy.array(t)


print ynew
print xnew
print tnew


matplotlib.pyplot.plot(xnew,tnew)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(ynew,tnew)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(xnew,ynew)
matplotlib.pyplot.show()
