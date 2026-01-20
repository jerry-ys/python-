x = "2 4 0 9 4 0 4 3 1 2 0 0 6 3 3 3 3 6 4 6 5 2 8 5 4 5 8 0 7 8 5 6 9 2 4 8 9 7 1 3 4 9 5 1 1 6 2 0 1 9 8 3 3 3 0 2 5 8 3 7 7 1 3 3 6 7 9 6 2 1 8 5 8 4 0 9 2 5 0 0 5 9 1 5 2 7 9 8 5 9 6 2 4 1 7 2 9 4 0 0"
data = []
for each in x.split():
    data.append(int(each))

max_sum = 0
for i in range(len(data)-2):
    _ = data[i] + data[i+1] + data[i+2]
    if _ > max_sum:
        max_sum = _

print(max_sum)