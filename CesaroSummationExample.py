import numpy as np
import matplotlib.pyplot as plt

k = 125
root_pi = np.sqrt(np.pi)


def s_k(t):
    res = 0
    for j in range(1, k+1):
        res += np.sin(j*t)
    return res/(root_pi*k)


x = np.linspace(-np.pi, np.pi, 1000)
y = s_k(x)
plt.xlim(-np.pi, np.pi)
plt.ylim(-1, 1)
plt.plot(x, y)
plt.savefig(f"CesaroSummation{k}.pdf")
