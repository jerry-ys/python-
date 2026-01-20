import requests
import bs4

def open_url(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}

    res = requests.get(url,headers = headers)
    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text,"html.parser")

    movies = []
    targets = soup.find_all("div",class_ = "hd")
    for each in targets:
        movies.append(f"{each.a.span.text} ")

    ranks = []
    targets = soup.find_all("span",class_ = "rating_num")
    for each in targets:
        ranks.append(f" {each.text} ")

    messages = []
    targets = soup.find_all("div",class_ = "bd")
    for each in targets:
        try:
            messages.append(f" {each.p.text.split("\n")[1].strip()+each.p.text.split("\n")[2].strip()}\n")
        except:
            continue

    '''
    evaluate = []
    targets = soup.find_all("p",class_ = "quote")
    for each in targets:
        evaluate.append(f"{each.span.text}\n")
    '''
        
    data = []
    for i in range(len(movies)):
        result = movies[i]+ranks[i]+messages[i]#+evaluate[i]
        data.append(result)
    return data

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    targets = soup.find("span",class_ = "next").find("a")
    if targets == None:
        return False
    else:
        link = targets.get("href")
        return link

def main():
    host = "https://movie.douban.com/top250"
    result = []
    link = ""
    while True:
        url = host + link
        res = open_url(url)
        link = find_depth(res)
        result.extend(find_movies(res))
        if link == False:
            break
    with open("movie.txt","w",encoding="utf-8") as f:
        for each in result:
            f.write(each)

if __name__ == "__main__":
    main()