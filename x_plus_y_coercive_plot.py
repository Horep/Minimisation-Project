import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = x


def h(x, y):
    return x*x + 3*x*y + y*y


X, Y = np.meshgrid(x, y)

Z = h(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap="coolwarm")
ax.view_init(10, 130)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$h$')
plt.tight_layout()
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.savefig("x_plus_y_coercive_plot.png", dpi=200)
