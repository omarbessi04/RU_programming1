stitch_numbers = {".":20, "O":10, "\\" : 25, "/": 25, "A": 35,"^": 5, "v": 22}

sum = 0
a, b = list(map(int, (input().split())))
for i in range(a):
    line = list(input())
    for symbol in line:
        if symbol in stitch_numbers:
            sum += stitch_numbers[symbol]

print(sum)
