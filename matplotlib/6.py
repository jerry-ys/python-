import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0.3,0.7,9).reshape(3,3)
print(a)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()