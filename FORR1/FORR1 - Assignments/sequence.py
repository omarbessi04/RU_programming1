# The sequence is adding the last 3 numbers together to get the next number
# Sequence always starts with [1, 2, 3] so start with those numbers
sequence = [1, 2, 3]

# Get input
num = int(input())
# Using addition, a for loop and right shift, generate the sequence into a list
for i in range(num):
    next_in_sequence = sequence[-3] + sequence[-2] + sequence[-1]
    sequence.append(next_in_sequence)

# Print the list, one item at a time
for i in range(num):
    print(sequence[i])