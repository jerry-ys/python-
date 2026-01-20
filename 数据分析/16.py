import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['B','C','D','E'],index=[2,3,4])
print(df1)
print(df2)
res = pd.concat([df1,df2],join='outer',ignore_index=True)
res1 = pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)
print(res1)
res2 = pd.concat([df1,df2.reindex(df1.index)],axis=1)
res3 = pd.concat([df1,df2],axis=1)
print(res2)
print(res3)
