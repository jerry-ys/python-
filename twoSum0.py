import random

nums = [random.randint(1,65535) for i in range(10000)]


target = int(input("请输入目标整数："))
n = len(nums)
for i in range(n):
    for j in range(n):
        if nums[i] + nums[j] == target:
            print([i,j])
