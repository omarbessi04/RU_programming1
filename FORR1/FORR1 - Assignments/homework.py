d = input().split(";")
sum = 0
for item in d:
    if "-" in item:
        d2 = item.split("-")
        sum += int(d2[1]) - int(d2[0]) + 1
    else:
        sum += 1


print(sum)