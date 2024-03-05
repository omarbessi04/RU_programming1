input_string = input("Input a string: ")
index = 0
reply = "a"

while index < len(input_string) - 1:
    if input_string[index] < input_string[index + 1]:
        reply = reply * 2
    else:
        reply = reply + input_string[index]

    index += 1

print(reply)