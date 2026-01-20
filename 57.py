import requests
import bs4
import re

def open_url(url):
    payload = {"q":"零基础入门学习python","sort":"sort=sale-desc"}
    url = "https://s.taobao.com/search"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
               "cookie":"cna=KAXsIB1AwSgBASQIgiAeJn3S; cdpid=UNGTrHtdhrtVMg%253D%253D; cnaui=3155427915; aui=3155427915; sca=a48015c1; tbsa=bd41d747355a970f3d1a0267_1755483491_11; atpsida=e6a85ae364c6d30f021297c2_1755483491_11"}
    res = requests.get(url,params=payload,headers = headers)

    return res

def main():
    keyword = input("请输入搜索关键词：")
    res = open_url(keyword)
    with open("tb.txt","w",encoding = "utf-8") as f:
        f.write(res.text)

if __name__ == "__main__":
    main()