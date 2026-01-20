import random

counts = int(input("请输入抛硬币的次数："))

# 利用 ignore 变量来判断是否打印每次的结果
if counts > 100:
    ignore = True
else:
    ignore = False

heads = 0 # 统计正面的次数
tails = 0 # 统计反面的次数

last = 0 # 记录上一次的状态，如果是正面设置为1, 反面则设置为2
c_heads = 0 # 统计连续正面的次数
c_tails = 0 # 统计连续反面的次数
max_heads = 0 # 统计连续正面的最多次数
max_tails = 0 # 统计连续反面的最多次数

i = 0
print("开始抛硬币实验……")
while i < counts:
    num = random.randint(1, 10)

    if num % 2:
        heads += 1
        c_heads += 1

        if not ignore:       
            print("正面", end=" ")

        # 如果上一次是反面：将连续正面的次数设置为1
        if last == 2:
            c_heads = 1

        # 判断连续正面的次数是否比max_heads大，如果是，取而代之
        if c_heads > max_heads:
            max_heads = c_heads

        # 将上一次的状态设置为正面
        last = 1
    else:
        tails += 1
        c_tails += 1
        
        if not ignore:
            print("反面", end=" ")

        # 如果上一次是正面：连续反面的次数设置为1
        if last == 1:
            c_tails = 1

        # 判断连续反面的次数是否比max_tails大，如果是，取而代之
        if c_tails > max_tails:
            max_tails = c_tails

        # 将上一次的状态设置为反面
        last = 2
        
    i += 1

print("")
print("一共模拟了", counts, "次抛硬币，结果如下：")
print("正面：", heads, "次", sep="")
print("反面：", tails, "次", sep="")
print("最多连续正面：", max_heads, "次", sep="")
print("最多连续反面：", max_tails, "次", sep="")
