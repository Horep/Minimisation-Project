import mpmath as mp
mp.dps = 400


def f(x):
    return mp.nsum(lambda n: mp.floor(n*x)/2**n, [1, mp.inf])


mp.plot(f, [0, 1.005], ylim=[0, 2], points=10000, file="devilsstaircase.pdf")
