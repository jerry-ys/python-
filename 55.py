import requests
import bs4
import re
import openpyxl

def open_url(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}
    res = requests.get(url,headers = headers)

    return res

def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    content = soup.find(id="mp-editor")
    targets = content.find_all("p")
    targets = iter(targets)

    for each in targets:
        if each.text.isnumeric():
            data.append([re.search(r'\[(.+)\]',next(targets).text).group(1),
                        re.search(r'\d.*',next(targets).text).group(),
                        re.search(r'\d.*',next(targets).text).group(),
                        re.search(r'\d.*',next(targets).text).group()])
    return data

def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市','平均房价','平均工资','房价工资比'])
    for each in data:
        ws.append(each)

    wb.save("2017年中国主要城市房价工资比排行榜.xlsx")

def main():
    url = "https://www.sohu.com/a/153364153_142115"
    res = open_url(url)
    data = find_data(res)
    to_excel(data)

if __name__ == "__main__":
    main()