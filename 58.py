import requests
import bs4
import json

def get_comments(url):

    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
               "referer":"https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&search_source=5&order=stow"
                }
    
    res = requests.get(url,headers = headers)
    return res

def convert_duration(duration_str):
    """
    将 "分钟:秒" 格式的时长转换为 "小时:分钟:秒" 格式
    例如: "1481:7" → "24:41:07"
    """
    try:
        # 分割分钟和秒
        minutes_str, seconds_str = duration_str.split(':')
        total_minutes = int(minutes_str)
        seconds = int(seconds_str)
        
        # 计算小时、剩余分钟
        hours = total_minutes // 60  # 总分钟数 ÷ 60 = 小时数
        remaining_minutes = total_minutes % 60  # 总分钟数 % 60 = 剩余分钟数
        
        # 格式化输出（确保两位数）
        return f"{hours:02d}:{remaining_minutes:02d}:{seconds:02d}"
    
    except (ValueError, IndexError) as e:
        return f"格式错误: {str(e)}"

def main():
    url = "https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&search_source=5&order=stow"
    res = get_comments(url)
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    data = res.json()  # 解析 JSON 数据
    #json_data = res.json()
    #comments = json_data["data"]["result"]
    with open("bili.txt", "w", encoding="utf-8") as file:
        file.write(res.text)
        '''for each in comments:
            file.write(each["title"]+":")
            file.write(each["arcurl"]+"\n")
            file.write(each["play"]+"/"+each["video_review"]+"/"+convert_duration(each["duration"])+"/"+each["author"])
            file.write("---------------------------------------\n")'''
        
if __name__ == "__main__":
    main()