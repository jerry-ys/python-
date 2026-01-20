# 题目要求：
# 请在此处补充装饰器 type_check() 的代码
def type_check(funA):
    def type_c(funB):
        def ty(n):
            if funA(n) == n:
                return funB(n)
            else:
                return "参数类型错误!"
        return ty
    return type_c

print("<<<--- 测试整数 --->>>")

@type_check(int)
def double(x):
    return x * 2

print(double(2))      # 这里打印结果应该是 4
print(double("2"))    # 这里打印结果应该是 “参数类型错误”


print("\n<<<--- 测试字符串 --->>>")

@type_check(str)
def upper(s):
    return s.upper()

print(upper('I love FishC.'))   # 这里打印结果应该是 I LOVE FISHC
print(upper(250))               # 这里打印结果应该是 “参数类型错误”
