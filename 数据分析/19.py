import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data1 = pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD"))
data1.cumsum()
print(data1.head())
data = data.cumsum()
data.plot()
plt.show()
data1.plot()
plt.show()
ax = data1.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data1.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)

plt.show()