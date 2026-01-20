import easygui as g
from pathlib import Path

path = g.diropenbox("请选择您的代码库")
def collect(x):
    filenum = 0
    lines = 0
    data = Path(path).glob(f"**/*{x}")
    for each in data:
        with open(each,"r",encoding='utf-8') as f:
            t = f.readlines()
            lines += len(t) - t.count("\n")
        filenum += 1
    return filenum,lines

context = f"【.py】源文件{collect(".py")[0]}个，源代码{collect(".py")[1]}行/n【.c】源文件{collect(".c")[0]}个，源代码{collect(".c")[1]}行/n【.cpp】源文件{collect(".cpp")[0]}个，源代码{collect(".cpp")[1]}行/n【.pas】源文件{collect(".pas")[0]}个，源代码{collect(".pas")[1]}行/n【.asm】源文件{collect(".asm")[0]}个，源代码{collect(".asm")[1]}行/n"
numbers = [collect(".py")[1],collect(".c")[1],collect(".cpp")[1],collect(".pas")[1],collect(".asm")[1]]
totallines = sum(numbers)
msg = f'您目前共编写了{totallines}行代码，完成进度：{(totallines / 100000):.2%}\n离10万行代码还差{100000-totallines}行，请继续努力！'
title = "统计结果"
g.textbox(msg,title,context)