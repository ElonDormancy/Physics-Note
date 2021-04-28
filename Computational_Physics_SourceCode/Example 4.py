import sympy as sy
import random
import matplotlib.pyplot as plt


def f(x):
    t = sy.symbols('t')
    g = sy.integrate(4/sy.pi**0.5*sy.exp(-t**2)*t**2, (t, x, sy.oo))
    return g


x0 = 0.5
y0 = 0.5
N = 1000
for i in range(N):
    x1 = round(random.uniform(0, 1), 2)
    w = f(x0)/f(x1)
    if w > 1:
        x2 = x1
    else:
        r = round(random.uniform(0, 2), 2)
        if r < w:
            x2 = x1
        else:
            x2 = x0
    x0 = x2

    y1 = round(random.uniform(0, 1), 2)
    s = f(y0)/f(y1)
    if s > 1:
        y2 = y1
    else:
        r = round(random.uniform(0, 2), 2)
        if r < s:
            y2 = y1
        else:
            y2 = y0
    y0 = y2
    plt.scatter(round(x0, 2), round(y0, 2), c="red")

plt.show()
