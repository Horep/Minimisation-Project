import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
x = np.linspace(-5, 5, 10000)


def phi(s):
    return np.floor(s)


def anti_derivative(x):
    return integrate.quad(phi, 0, x)

y = []

for s in x:
    y.append(anti_derivative(s))
plt.plot(x, y)