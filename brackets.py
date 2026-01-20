s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []

for c in s:
    if c == '(' or c == '[' or c == '{':# 如果是左括号 #:
        stack.append(c)# 那么添加到特殊列表中 #
    else:
        if len(stack) == 0:
            print("非法T_T")
            break

        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'

        if d != stack.pop():# 对比 d 和从特殊列表尾部弹出的元素 #:
            print("非法T_T")
            break
else:
    if len(stack) == 0:
        print("合法T_T")
    else:
        print("非法T_T")
