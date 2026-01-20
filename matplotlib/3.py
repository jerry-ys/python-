import matplotlib.pyplot as plt
import numpy as np

X = np.arange(12)
Y1 = (1-X/float(12))*np.random.uniform(0.5,1,12)
Y2 = (1-X/float(12))*np.random.uniform(0.5,1,12)

plt.bar(X,Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x,y+0.05,f'{y:.2f}',ha='center',va='bottom')

for x,y in zip(X,Y2):
    plt.text(x,-y-0.05,f'{y:.2f}',ha='center',va='top')

plt.xlim(-.5,12)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()