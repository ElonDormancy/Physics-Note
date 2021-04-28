import numpy as np
import matplotlib.pyplot as plt

h = 0.1
N = 30
dt = 0.0001
M = 10000
A = dt/h**2
U = np.zeros([N+1, M+1])

space = np.arange(0, (N+1)*h, h)


for k in np.arange(0, M+1):
    U[0, k] = 0
    U[N, k] = 0

for i in np.arange(0, N):
    U[i, 0] = 4*h*i*(3-i*h)

for k in np.arange(0, M):
    for i in np.arange(0, N):
        U[i, k+1] = A*U[i+1, k]+(1-2*A)*U[i, k]+A*U[i-1, k]


extent = [0, 1, 0, 3]  # 时间和空间的取值范围
levels = np.arange(0, 10, 0.1)
plt.contourf(U, levels, origin='lower', extent=extent, cmap=plt.cm.jet)
plt.ylabel('x', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.show()

