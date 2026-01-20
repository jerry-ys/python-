s = input("请输入一个由字母构成的字符串：")
    
n = len(s)
for i in range(1, n//2+1):
    # 如果子字符串的长度为i，则n必须可以被i整除才行
    if n % i == 0:
        # 如果子字符串的长度为i，则i到i*2之间是一个重复的子字符串
        if s.startswith(s[i:i*2]) and s.count(s[i:i*2]) == n/i:
            print(True)
            break
# for...else的用法，小甲鱼希望大家还没有忘记哦^o^
else:
    print(False)
