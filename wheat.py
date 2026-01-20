i = 1
s = 0

while i <= 64:
    wheats = pow(2, i-1)
    s = s + wheats
    i = i + 1

print("舍罕王应该给达依尔", s, "粒麦子！")
