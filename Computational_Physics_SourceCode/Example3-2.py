from sympy import *

Pi = 3.1415926535898


def L(n, k, a, b):
    x = symbols('x')
    h = (b-a)/n
    prob = 1
    for i in range(n+1):
        if i == k:
            pass
        else:
            prob = prob*(x - (a+i*h))/(k*h-i*h)
    return integrate(prob, (x, a, b))


def f(x):
    g = sin(x)
    return g


def P(n, a, b):
    h = (b-a)/n
    p = 0
    for i in range(n+1):
        p = p + f(a+i*h)*L(n, i, a, b)
    return p


def Composite(n, m, a, b):
    s = (b-a)/m
    r = 0
    for i in range(m):
        r = r + P(n, a+i*s, a+(i+1)*s)
    return r


print(Composite(1, 360, 0, Pi))
print(Composite(2, 18, 0, Pi))
