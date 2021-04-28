def a(x):
    v1= x - x**3 -4*x**2 +10
    return v1
def b(x):
    v2= 0.5*(10-x**3)**0.5
    return v2

def iteration(x):
    for i in range(100):
        x = b(x)
    print(x)

iteration(1.5)