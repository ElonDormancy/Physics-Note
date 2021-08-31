import numpy as np
import inte  #fortran compiled module
x=np.arange(0,1,0.001)
fx=4/(1+x**2)
print (inte.rect_inte(fx,0,1)) 
print (inte.trap_inte(fx,0,1))
print (inte.simp_inte(fx,0,1))
