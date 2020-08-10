import matplotlib.pyplot as plt
from math import *
import numpy
N = 5
n = list(range(0,N+1))
r = 15
thetha = radians(90)
centro = 0

x = []
for i in n:
    x.append(r*cos((2*pi*i/N)+thetha)+centro)

y = []
for i in n:
    y.append(r*sin((2*pi*i/N)+thetha)+centro)

print(x,y)
plt.plot(x,y)
plt.show()
