from sympy import *
Pi = 3.1415926535


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
    g = 4/(1+x**2)
    return g


def P(n, a, b):
    h = (b-a)/n
    p = 0
    for i in range(n+1):
        p = p + f(a+i*h)*L(n, i, a, b)
    return p


print(f"Trapezoidal rule method result{P(1, 0, 1)}")  # Trapezoidal rule
print(f"Simpson's rule method result {P(2, 0, 1)}")  # Simpson's rule.
print(abs(P(1, 0, 1)-Pi)/Pi)
print(abs(P(2, 0, 1)-Pi)/Pi)
