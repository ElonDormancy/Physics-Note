from sympy import *
pi = 3.1415926535


def f(x):
    g = cos(x) - x
    return g


def f_1(x):
    t = symbols('t')
    expr = diff(cos(t) - t, t)
    return expr.subs(t, x)


def Bisection(a, b):
    p = a+(b-a)/2
    if -1e-8 < f(p) < 1e-8:
        print(p)
    else:
        if f(a)*f(p) > 0:
            a = p
            return Bisection(a, b)
        else:
            b = p
            return Bisection(a, b)


def fix_point(x):
    for i in range(50):
        x = f(x) + x
    print(x)


def Newton(x):

    for i in range(50):
        x = x - f(x)/(f_1(x))
    print(x)


def Secant(x0, x1):
    for i in range(50):
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        if abs(x2-x0) < 0.00000001:
            break
    print(x2)


Bisection(0.5, 0.8)
fix_point(0.74)
Newton(pi/4)
Secant(0.5, 0.8)
