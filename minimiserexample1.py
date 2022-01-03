import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 4000)
y = x


def F(x, y):
    first = x**2 + y**2
    second = np.exp(x*x + y*y - x*y)/10000
    return np.maximum(first, second)


X, Y = np.meshgrid(x, y)

Z = F(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap="coolwarm")
ax.view_init(20, 130)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$F$')
plt.savefig("minimiserexample1.png", dpi=200)
