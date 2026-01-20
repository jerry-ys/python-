import hashlib
data = {}
x = "021bbc7ee20b71134d53e20206bd6feb"
y = "e10adc3949ba59abbe56e057f20f883e"
z = "655d03ed12927aada3d5bd1f90f06eb7"

for i in range(1000000):
    data[i] = hashlib.md5(bytes(str(i),"utf-8"))

for each in data:
    if data[each].hexdigest() == x:
        print(each)
    elif data[each].hexdigest() == y:
        print(each)
    elif data[each].hexdigest() == z:
        print(each)
