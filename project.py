words = ["Twitter", "TOTO", "FishC", "Python","ASL"]

q = "QWERTYUIOPqwertyuiop"
a = "ASDFGHJKLasdfghjkl"
z = "ZXCVBNMzxcvbnm"

for each in words:
    if each[0] in q:
        for i in each:
            if i not in q:
                words.pop(words.index(each))
                break
    elif each[0] in a:
        for i in each:
            if i not in a:
                words.pop(words.index(each))
                break
    elif each[0] in z:
        for i in each:
            if i not in z:
                words.pop(words.index(each))
                break
    else:
        print(words)
print(words)
        

