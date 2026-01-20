try:
    1/0
except BaseException as e:
    print("打错啦")
    print(e)
