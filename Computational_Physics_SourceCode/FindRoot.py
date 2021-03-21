import matplotlib.pyplot as plt
import numpy as np
def f(x):
    f = x**3+4*x**2-10
    return f

def findroot(a,b):
    p = a+(b-a)/2
    if -1e-8<f(p) < 1e-8 :
        return p
    else:
        if f(a)*f(p) >0 :
            a = p
            return findroot(a,b)
        else:
            b = p
            return findroot(a,b)

#plot
x=np.linspace(1,2,500)
plt.xlim((1, 2))
plt.ylim((-10, 10))
plt.grid(True)
plt.tight_layout(0.5)
plt.plot(x,f(x))
plt.show()
print(findroot(1,2))