def frange(start=0.0, stop=None, step=0.1):
    if stop == None:
        start,stop = 0.0,start
    current = start
    while current < stop:
        yield current
        current += step
        current = round(current,1)


def frange(start, stop=None, inc=0.1):
    s = str(inc)
    pre = len(s[s.find('.')+1:])
    start += 0.0 # 确保start变成浮点数

    if stop == None:
        stop = start + 0.0  # 确保stop变成浮点数
        start = 0.0

    while start < stop:
        yield round(start, pre)
        start += inc
