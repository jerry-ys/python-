from pathlib import Path
    
def get_files(p, files):
    for each in p.iterdir():
        if str(each) == __file__:
            continue
        if each.is_file() and each.suffix == '.py':
            files.append(each)
        if each.is_dir():
            p = each
            get_files(p, files) # 此处使用递归搜索会更方便
    
    return files
    
    
def count_lines(files):
    lines = 0
    for each in files:
        with open(each, "r", errors="ignore") as f:
            t = f.readlines()
            lines += len(t) - t.count('\n') # 空行不能算，所以要减去空行数量
    
    return lines
    
    
p = Path.cwd()
files = []
    
files = get_files(p, files)
print(f"一个有 {count_lines(files)} 行代码~")
