import wordcloud

file = open("最多收藏.txt",encoding = "utf-8")
text = file.read()
stopwords = {"野生技术协会", "编程", "教育", "讲座", "编程技术宅", "教学", "电脑", "技术", "编程教育", "编程入门", "开发", "科学", "演示", "软件", "编程视频教程", "编程课程", "教学视频", "经验分享", "IT", "编程语言", "编程学习", "互联网", "考试", "考研", "科技", "语言", "技术宅", "面试", "自学", "原创", "公开课", "程序员", "学习", "课程", "教程", "计算机", "线上课堂", "视频教程"}
wc = wordcloud.WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",stopwords = stopwords)
wc.generate(text)
image = wc.to_image()
image.show()
