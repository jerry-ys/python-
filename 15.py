while True:
    try:
        x = input("请输入一行语句：")
        y = eval(x)
        if y:
            print(f"结果是：{y}")
    except SyntaxError:
        print("错误：语法错误")
    except IndexError:
        print("错误：索引错误")
    except NameError:
        print("错误：变量未定义")
    except ZeroDivisionError:
        print("错误：除数为0")
    except ValueError:
        print("错误：传入的参数类型不恰当")
    except KeyboardInterrupt:
        print("程序结束~")
        break
