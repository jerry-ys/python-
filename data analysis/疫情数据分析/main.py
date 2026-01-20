import numpy as np
import matplotlib.pyplot as plt

with open("covid19_day_wise.csv","r",encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date":[],
    "data":[],
    "header":[h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])

print(covid["header"])
print(covid["data"][:5])
print(covid["date"][:5])

data = np.array(covid["data"])

# 获取某日的所有数据(row的index)
date_idx = covid["date"].index("2020-02-03")
for header,number in zip(covid['header'],data[date_idx]):
    print(f"{header}:{number}")

# 截止日期之前的累计确诊病例有多少(column的index)
row_idx = covid["date"].index("2020-02-03")
column_index = covid['header'].index("Confirmed")
confirmed0124 = data[row_idx,column_index]
print("截止1月24日的累积确诊数:", confirmed0124)

# 2020 年 7 月 23 日的新增死亡数是多少？
row_index = covid["date"].index("2020-07-23")
column_index = covid["header"].index("New deaths")
result = data[row_index,column_index]
print("截止7月23日的新增死亡数:", result)

# 从 1 月 25 日到 7 月 22 日，一共增长了多少确诊病例？
row1 = covid["date"].index("2020-01-25")
new_cases = covid["header"].index("New cases")
row2 = covid["date"].index("2020-07-22")
result = data[row1+1:row2+1,new_cases].sum()
print("共新增：", result)

confirmed_idx = covid["header"].index("Confirmed")
comfirmed = data[:,confirmed_idx]
new_case = data[:,new_cases]
for i in range(row1,row2+1):
    diff = new_case[i] - (comfirmed[i]-comfirmed[i-1])
    if diff != 0:
        print("date index:", i, ";差异：", diff)

# 每天新增确诊数和新恢复数的比例？平均比例，标准差各是多少？
new_cases_idx = covid["header"].index("New cases")
new_recovered_idx = covid["header"].index("New recovered")
ratio = data[:,new_cases_idx] / data[:,new_recovered_idx]
print("比例样本",ratio[:5])
print(data[0,new_cases_idx])
print(data[0,new_recovered_idx])
not_zero_mask = data[:,new_recovered_idx] != 0
ratio = data[not_zero_mask,new_cases_idx] / data[not_zero_mask,new_recovered_idx]
ratio_mean = ratio.mean()
ratio_std = ratio.std()
print("平均比例：", ratio_mean, "；标准差：", ratio_std)

# 画图展示新增确诊的变化曲线
new_cases_idx = covid["header"].index("New cases")
plt.plot(data[:,new_cases_idx])
plt.show()
print(covid["date"][50])

# 画图展示死亡率的变化曲线
death_ratio_idx = covid["header"].index("Deaths / 100 Cases")
plt.plot(data[:,death_ratio_idx])
plt.show()