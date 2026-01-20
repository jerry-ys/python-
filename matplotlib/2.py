import matplotlib.pyplot as plt
import numpy as np

X = np.random.normal(0,1,1024)
Y = np.random.normal(0,1,1024)
T = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# plt.scatter(np.arange(5),np.arange(5))

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks([])
plt.yticks(())
plt.show()