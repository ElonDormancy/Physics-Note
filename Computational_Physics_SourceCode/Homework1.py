import matplotlib.pyplot as plt
import numpy as np
# Recurrence Relation


def Bessel(x, n, m):
    if n >= m:
        return 0
    elif n == m-1:
        return 1
    else:
        return -Bessel(x, n+2, m) + 2*(n+1)*Bessel(x, n+1, m)/x


coefficient = 0
# Sum to normalized


def normailzed(x, m):
    sum = Bessel(x, 0, m)**2
    for i in range(1, m+1):
        sum += 2*Bessel(x, i, m)**2

    coefficient = (1/sum)**0.5

    return coefficient
# Plot BesselFunction
x = np.linspace(1e-15, 30, 500)
for v in range(0, 11):
    plt.plot(x, normailzed(x, 20)*Bessel(x, v, 20))
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
