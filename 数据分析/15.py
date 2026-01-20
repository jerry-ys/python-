import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
print(df1)
print(df2)
print(df3)
res = pd.concat([df1,df2,df3],axis = 0,ignore_index=True)
print(res)