file = open(input())

for line in file:
    new_line = ""
    line = line.split()
    for word in line:
        new_line += f"{word[::-1]} "
    print(new_line)
