# From given list, print the list, check the list for integers, and print missing integers

def find_integers_in_list(list):
    """Return a list of the integers in the string (unsorted)"""
    integers_in_string = []
    for item in list:
        if item.isnumeric():
            integers_in_string.append(int(item))
            
    return integers_in_string

def find_missing_ints(list, largest_num):
    """Return a sorted list of the missing integers starting at 0 and ending with the largest int in the input string"""
    missing_integers = []
    for i in range(largest_num):
         if not(i in list):
              missing_integers.append(i)

    return missing_integers


input_string_list = input().split()
# Print the given input
print(input_string_list)

# Find all the integers in the input and print them
integers_in_input = find_integers_in_list(input_string_list)
print(integers_in_input)

# If there are integers in the input, print the missing integers

if integers_in_input != []:
    LARGEST_NUMBER_IN_INPUT_STRING = max(integers_in_input)
else:
    LARGEST_NUMBER_IN_INPUT_STRING = 0
    
missing_integers = find_missing_ints(integers_in_input, LARGEST_NUMBER_IN_INPUT_STRING)
print(missing_integers)
