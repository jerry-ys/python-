import easygui as g
from pathlib import Path

path = g.fileopenbox(default = '*.txt')
x = Path(path)
msg = f"文件【{x.name}】的内容如下："
title = "显示文件内容"

with open(path,"r",encoding = "utf-8") as f:
    _ = f.read()
    context = g.textbox(msg,title,_)

choices = ("覆盖保存","放弃保存","另存为...")
msg = "检测到文件内容发生改变，请选择以下操作："
title = "警告"
if context == _:
    pass
else:
    ins = g.buttonbox(msg,title,choices)
    if ins == choices[0]:
        with open(path,"w",encoding = "utf-8") as f:
            f.write(context)
    elif ins == choices[1]:
        pass
    elif ins == choices[2]:
        file = g.filesavebox(default = "*.txt")
        with open(file,"w") as f:
            f.write(context)