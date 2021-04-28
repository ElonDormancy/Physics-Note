from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def GET(fs, N):
    # define sampled frequency:
    T = N/fs
    h = T/N
    x = []
    for l in range(N):
        x.append(f(l*h).evalf(3))
    return x


def f(x):
    g = sin(2*pi*x)
    return g

# Method 1


def DFT1(x, fs):
    w = 0
    y = []
    p = []
    # DFT:
    for j in range(fs):
        for i in range(fs):
            w = w + x[i]*(cos(2*pi*(j)*i/fs) - I*sin(2*pi*(j)*i/fs)).evalf()
        y.append(w)
        w = 0
    for o in y:
        p.append(abs(o**2))
    return p
# Method 2


def DFT2(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    p = []
    for o in np.dot(M, x).reshape(N, 1):
        p.append(abs(o**2))
    return p


x = []
for i in range(8):
    x.append(i)
plt.scatter(x, DFT1(GET(8, 8), 8), c="red")
plt.scatter(x, DFT2(GET(8, 8)), c="blue")
plt.show()
