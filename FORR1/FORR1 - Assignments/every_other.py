string = input()
i = 0
other_letter = []
for letter in string:
    if i == 0:
        other_letter.append(letter)
        i = 1
    else:
        i = 0
print("".join(other_letter))