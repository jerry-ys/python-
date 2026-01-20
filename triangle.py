# 初始化杨辉三角形
# 创建一个10*10的二维列表，并将所有的元素初始化为0
triangle = []
for i in range(10):
    triangle.append([])
    for j in range(10):
        triangle[i].append(0)
    
# 计算杨辉三角形
# 根据观察，我们知道杨辉三角形左右两边的元素均为1
for i in range(10):
    triangle[i][0] = 1
    triangle[i][i] = 1
    
# 第i行j列的值 = 第(i-1)行(j-1)列的值 + 第(i-1)行(j)列的值
for i in range(2, 10):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
# 输出杨辉三角形
for i in range(10):
    # 因为是三角形，所以i越小，前边需要填充的TAB越多
    for k in range((10-i)//2):
        print('\t', end='')
    for j in range(i+1):
        # 要形成“隔行错开”的效果，所以我们在偶数行加4个空格
        if i % 2 == 1:
            print("    ", end='')
        # 为何要使用TAB而非空格，大家可以将下面的end='\t'改成对应的空格数即可知晓
        print(triangle[i][j], end='\t')
    print()
