# Program that analyses sequence from text file

# First we define functions

# Function 1: Adds up the cumulative sum of a sequence
def cumulative_sum(sequence):
    sum = 0
    cumulative_sum_list = []

    for num in sequence:
        sum += num
        cumulative_sum_list.append(sum)
    
    return(cumulative_sum_list)


# Function 2: Returns a sorted sequence
def getSortedList(sequence):
    return sorted(sequence)


# Function 3: Returns a median of a sequence
def getMedian(sequence):

    # Medians differ when there is already a set "middle" and when there is not
    # In other words, if the length of the sequence is odd or not

    length_of_list = len(sequence)
    
    if length_of_list % 2 == 0:

        # If there isn't a set middle, calculate the average of the 2 middle numbers

        middle1 = sequence[length_of_list // 2 - 1]
        middle2 = sequence[length_of_list // 2]

        median = (middle1 + middle2)/2

        return median
    
    else:
        # If there is a set "middle" number, return that
        index = ((length_of_list+1)//2)-1
        median = sequence[index]
        return median

# Function 4: Rounds numbers in a sequence
def roundNumbers(sequence):
    rounded_sequence = []

    for num in sequence:
        rounded_num = round(num, FLOATING_POINT_PRECISION)
        rounded_sequence.append(rounded_num)

    return rounded_sequence



FLOATING_POINT_PRECISION = 4
file_name = input()
good_numbers = []

# First check if the file can be opened
try:
    file = open(file_name)
    run = True
except:
    run = False

# Then check if there are legal floats in the file
if run:
    for line in file:
        try:
            line = float(line)
            good_numbers.append(line)

        except:
            continue

# If there are no legal floats in the file, don't do more
if good_numbers != []:
 
    # 4 things to output:

    # 1 . The numbers in the sequence
    rounded_good_numbers = roundNumbers(good_numbers)
    print(*rounded_good_numbers)

    # 2. The cumulative sum of the numbers in the sequence
    sum_list = cumulative_sum(good_numbers)
    rounded_sum_list = roundNumbers(sum_list)
    print(*rounded_sum_list)

    # 3. The sorted version (ascending order) of the numbers in the sequence
    sorted_good_numbers = getSortedList(good_numbers)
    rounded_sorted_good_list = roundNumbers(sorted_good_numbers)
    
    print(*rounded_sorted_good_list)

    # 4. The median of the sequence
    median = getMedian(sorted_good_numbers)
    median = round(median, FLOATING_POINT_PRECISION)
    print(median)