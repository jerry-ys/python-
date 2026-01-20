import pandas as pd

left = pd.DataFrame({
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})


right = pd.DataFrame({
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

print(left)
print(right)
print(boys)
print(girls)
res1 = pd.merge(left, right, on=["key1", "key2"])
res2 = pd.merge(left, right, on=["key1", "key2"],how='outer',indicator=True)
res5 = pd.merge(left, right, on=["key1", "key2"],how='outer',indicator='可以换名字')
res3 = pd.merge(left, right, on=["key1", "key2"],how='left')
res4 = pd.merge(left, right, on=["key1", "key2"],how='right')
res6 = pd.merge(left, right, left_index=True,right_index=True,how='outer')
res7 = pd.merge(left, right, left_index=True,right_index=True,how='inner')
res8 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
res9 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)