import pandas as pd

data = pd.read_csv(r'C:\Users\a1523\Desktop\python\数据分析\test.csv',sep='\t')
print(data)

data.to_pickle('student.pickle')