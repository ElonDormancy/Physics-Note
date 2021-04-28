import numpy as np
import matplotlib.pyplot as plt


def f(z, i, N):
    g = np.exp(1j*z*np.cos(2*np.pi*i/N))
    return g


def generatesq(z, N):
    s = []
    for m in range(N):
        s.append(f(z, m, N))
    return s


def DFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(2j * np.pi * k * n / N)
    return np.dot(M, x).reshape(N, 1)


def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized set 32
        return DFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)
        s = np.concatenate([X_even + factor[:N / 2] * X_odd,
                            X_even + factor[N / 2:] * X_odd])
    return s


def normalize(z, N):
    x = generatesq(z, N)
    b = []
    for i in range(len(DFT(x))):
        b.append(1j**(-i)*FFT(x)[i]/N)
    return b


'''
def printf(z, N):
    k = []
    for i in range(N):
        l = normalize(generatesq(z, N), i, 1, N)[0][0]
        k.append(l)
    return k

'''


def clear(x, N):
    y = []
    for i in x:
        y.append(normalize(i, N))
    y = np.array(y)
    return y


def gety(N, a, b, n):
    x = np.linspace(a, b, n)
    y1 = np.zeros(shape=(N, n))

    for i in range(n):
        for j in range(len(clear(x, N)[i].reshape(1, N)[0])):
            y1[j][i] = clear(x, N)[i].reshape(1, N)[0][j]
    return y1


x = np.linspace(0, 10, 100)
yf = gety(2**3, 0, 10, 100)
plt.xlim((0, 10))
plt.ylim((-1, 1.1))
for i in range(2**3):
    plt.plot(x, yf[i])
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$',
            '${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$',
            '${J}_6(x)$', '${J}_7(x)$'), loc=0)
plt.xlabel('$x$', fontsize="12")
plt.ylabel('${J}_n(x)$', fontsize="12")
plt.grid(True)
plt.tight_layout(0.5)
plt.show()
