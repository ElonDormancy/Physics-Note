import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spl
x = np.linspace(0, 30, 500)
for i in range(11):
    y = spl.jv(i, x)
    plt.plot(x, y)
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
