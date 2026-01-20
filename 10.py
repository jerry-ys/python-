def fib():
    back1, back2 = 0, 1
    def func():
        nonlocal back1, back2
        temp = back1
        back1, back2 = back2, back1 + back2
        return temp
    return func
        
