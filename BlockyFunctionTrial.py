import numpy as np
import matplotlib.pyplot as plt

n = 3


def phi(t):
    t2 = 2**n * t
    # range needs an extra term in the upper limit due to how python works
    for k in range(0, 2**(n-1) - 1 + 1):
        if 2*k < t2 < 2*k + 1:
            return 1
    return 0


def z(t):
    return 1


x = np.linspace(0, 1, 200000)
y = []

for t in x:
    y.append(z(t)*phi(t))


fig, ax = plt.subplots()
plt.xlim(0, 1)
plt.xticks([0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1])
ax.set_xticklabels([r"$0$", r"$\frac{1}{8}$", r"$\frac{1}{4}$",
                    r"$\frac{3}{8}$", r"$\frac{1}{2}$", r"$\frac{5}{8}$",
                    r"$\frac{3}{4}$", r"$\frac{7}{8}$", r"$1$"])
ax.set_aspect('equal', adjustable='box')
plt.fill_between(x, y, color=(200/256, 63/256, 63/256, 0.8))
plt.tight_layout()
plt.grid()
plt.plot(x, y)
plt.savefig(f"BlockyWeakConvergence{n}.png", dpi=1000)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=12)
