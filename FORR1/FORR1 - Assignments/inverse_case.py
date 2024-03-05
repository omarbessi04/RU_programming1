string = list(input())
new_string = []
for letter in string:
    if letter == letter.lower():
        new_string.append(letter.upper())
    else:
        new_string.append(letter.lower())
print("".join(new_string))