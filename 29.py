import urllib.request
import chardet

URL = input("请输入URL：")
x = urllib.request.urlopen(URL).read()

def check(x):
    if chardet.detect(x)['encoding'] == "GB2312":
        print("该网页使用的编码是：GBK")
    else:
        print(f"该网页使用的编码是：{chardet.detect(x)['encoding']}")

check(x)




    
