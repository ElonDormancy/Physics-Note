import random
Pi = 3.14159265358979
m = 10
N = 1000000
a = 0
b = 0
for j in range(m):
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            a = a + 1
        else:
            a = a
    b = a+b
print(f"Result = {4*a/(m*N)}")
print(f"{abs(4*a/(m*N)-Pi)/Pi}")
