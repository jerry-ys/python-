n = int(input("请输入一个自然数："))

while n > 0:
    if n % 2 == 0:
        print(n,"/2=",int(n/2),sep = "")
        n = int(n / 2)
    else:
        print(n,"*3+1=",n*3+1,sep = "")
        n = n * 3 + 1
    if n == 1:
        break
