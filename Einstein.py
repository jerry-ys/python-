# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-150254-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) 2020 fishc.com.cn All rights reserved

# 由于目标值必须是能被7整除，所以我们将测试每个7的倍数
steps = 7
i = 1
FIND = False

while i < 100:
    # 由于测试的都是7的倍数
    # 因此只要同时满足除以2余1、除以3余2、除以5余4、除以6余5，就是最终的结果
    if (steps % 2 == 1) and (steps % 3 == 2) and (steps % 5 == 4) and (steps % 6 == 5):
        FIND = True
        break
    else:
        steps = 7 * (i + 1)
    i = i + 1

if FIND == True:
    print('阶梯数是：', steps)
else:
    print('在程序限定的范围内找不到答案！')
