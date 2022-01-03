import mpmath as mp
import numpy as np
import matplotlib.pyplot as plt
mp.mp.dps = 50


def phi(x):
    return mp.nsum(lambda n: mp.floor(n*x)/2**n, [1, mp.inf])


num = 10000
y = []
for i in range(0, num+1):
    y.append(phi(i/num))

x = np.linspace(0, 1 ,num+1)

y2 = []

for m in range(0, num+1):
    res = 0
    for k in range(0, m):
        res += y[k]
    y2.append(res/num)
  
plt.grid()
plt.xlim(0,1)
plt.ylim(0,0.5)
plt.plot(x, y2)
plt.savefig("devilsstaircaseintegral.pdf")
