run = True
max_int = 0
# Establish while loop
while run:

# Get input
    num = int(input())

# If input is negative, then stop the program
    if num < 0:
        run = False

# If input is positive, then check if it the largest input so far
    else:
        if num > max_int:
# If it is, then it becomes the "max_int"
            max_int = num
# Finally, print the max_int
print(max_int)