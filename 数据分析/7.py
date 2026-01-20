import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
print(A)
x = np.array([6,6,6])
print(x)
print(x[np.newaxis,:])

C = np.vstack((A,B))
D = np.hstack((A,B))
E = np.concatenate((A,B,B,A),axis=1)
print(E)

print(D)
print(A.shape,C.shape,D.shape)
