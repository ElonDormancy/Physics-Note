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


def DFT(x, n):
    w = 0
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    y = []
    # DFT:
    for k in range(N):
        w = w + x[k]*(1j**(-n)/N)*np.exp(2*np.pi*1j*n*k/N)
    y.append(w)
    return y


x = np.linspace(0, 30, 500)
for i in range(11):
    y = DFT(generatesq(x, 2**12), i)[0]
    plt.plot(x, y)
print(inpu)
plt.xlim((0, 30))
plt.ylim((-0.5, 1.1))
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$',
            '${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$',
            '${J}_6(x)$', '${J}_7(x)$', '${J}_8(x)$',
            '${J}_9(x)$', '${J}_{10}(x)$'), loc=0)
plt.xlabel('$x$', fontsize="12")
plt.ylabel('${J}_n(x)$', fontsize="12")
plt.grid(True)
plt.tight_layout(0.5)
plt.show()
