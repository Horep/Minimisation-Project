import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
x = np.linspace(0, 5, 100000)

y = gamma(x)
y2 = np.log(y)
plt.ylim(-1, 10)
plt.xlim(0, 5)
plt.grid()
plt.plot(x, y, label=r"$\Gamma$")
plt.plot(x, y2, label=r"$\ln(\Gamma)$")
plt.legend()
plt.savefig("GammaFunction.pdf")
