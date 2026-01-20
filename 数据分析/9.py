import numpy as np

a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b)
print(d)
d[1:3] = [22,33]
print(a)
b = a.copy()
print(b)
a[3] = 44
print(a)
print(b)