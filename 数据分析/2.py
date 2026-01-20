import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
c = a-b
print(c)
c = a+b
print(c)
c = a * b
print(c)
c = b**2
print(c)
c = 10*np.sin(a)
print(np.sin(3.14))
print(c)
print(b<3)
print(b==3)