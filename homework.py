s = input("请输入待压缩字符串：")

ch = s[0]
result = ''
count = 0

for each in s:
    if each == ch:
        count += 1
    else:
        if count > 2:
            result += ch + str(count)
        if count == 2:
            result += ch + ch
        if count == 1:
            result += ch
        ch = each
        count = 1

if count == 1:
    result += ch
else:
    result += ch + str(count)

print(f"压缩后的字符串：{result}")
print(f"压缩率为：{len(result)/len(s)*100:.2f}%")
                
    

    
