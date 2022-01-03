import numpy as np
import matplotlib.pyplot as plt

M = 1000000


def weierstrass(x, N):
    y = np.zeros((1, M))
    for n in range(1, N):
        y = y + np.cos(3**n*np.pi*x)/2**n
    return y + np.cosh(x)


x = np.linspace(-2, 2, M)
y = np.reshape(weierstrass(x, 600), (M, ))

plt.plot(x, y, linewidth=0.1)
plt.savefig("Wigglycosh.pdf")
plt.show()
