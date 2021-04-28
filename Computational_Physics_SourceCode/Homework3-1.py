import numpy as np


def DFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


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
        factor = np.exp(-2j*np.pi*np.arange(N) / N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])
    return X


def iDFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(np.linalg.inv(M), x).reshape(N, 1)


def iFFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized set 32
        return iDFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N) / N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])
    return X


def CFFT(x, ISIGN):
    if ISIGN == 1:
        a = FFT(x)
    elif ISIGN == -1:
        a = iFFT(x)
    else:
        print("Please input the correct parameter")
    return a
