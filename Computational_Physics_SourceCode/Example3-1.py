from sympy import *

Pi = 3.1415926


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


print(P(1, 0, Pi/4))
print(P(2, 0, Pi/4))
print(P(3, 0, Pi/4))
