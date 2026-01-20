import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns=['a','b','c','d'])
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
df2 = pd.DataFrame({'A':1.,
                    'first':pd.Timestamp('20250903'),
                    'second':pd.Series(1,index=range(4)),
                    'third':np.array([3]*4,dtype='int32'),
                    'forth':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})

print(dates)
print(df)
print(df1)
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values(by='forth'))