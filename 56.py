import requests
import json

def get_comments(url):

    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
               "referer":"https://music.163.com/album?id=3428868"
                }
    
    params = "U7vnfEKuXCHiaCFus9B3pUK2q5YBdGX2Q+sJlaiplzpcYG+4nwb9mgR76mu+N2SuOcPNEPbALSE34FvU3KRB5GycwhJTApN+AObYukYX1jk6qAHSOJfQccC2ohaHgX8Gafo5qfpwxKdxaGlDvYlBFmVibQ2hOv7Y6JTZ/UPEw71Rh3xNl1IWhUOjogbSAxwEUQoQLjHBnYfJMW3UiqTHwo5W13YJkJpWIqX2FHU2G+hgObnwQJM3om8UrqRuGIKRyFfuY38r5prbK9g/xo+1zP65G0xHheP0trTFn1ohxGKxSAfO7EnXGhMJ1pViPHOL"
    encSecKey = "aa62d0378ce672a72076fedcaabee06379c7e688100f405b1b55184ed1e6902c01bdfded61a3f961e19cc30623f40ae2fbc98d57d21b473fe1953264f3deaef088ccbe84a7805f797e02904239dc9d9e3beb56394c4231ff49a6719d2fd059df47615b3f4147d0aa03043f9004377c9cec17278c2452e46f384018232dbfe01c"
    data = {
        "params":params,
        "encSecKey":encSecKey
        }

    res = requests.post(url,headers = headers,data = data)

    return res

def main():
    url = input("请输入链接地址：")
    res = get_comments(url)
    json_data = res.json()
    comments = json_data["data"]["comments"]
    with open("comments.txt", "w", encoding="utf-8") as file:
        for each in comments:
            file.write(each["user"]["nickname"]+":\n\n")
            file.write(each["content"]+"\n")
            file.write("---------------------------------------\n")
        
if __name__ == "__main__":
    main()