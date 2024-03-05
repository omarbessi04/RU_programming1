def is_prime(num):
    if num < 2:
        return(False)
    else:
        for i in range(2, num):
            if (num % i) == 0:
                return(False)
    return(True)

# Get input stop_range
stop_range = int(input())

# Get input num_divisors
num_divisors = int(input())

# Establish for loop that finds positive 2 digit numbers smaller than stop_range
for i in range(10,stop_range):
# Find numbers which this rule applies to:  xy = (x+y)**2
    i = str(i)
    if (int(i[0]) + int(i[1]))**2 == int(i):
# Print those numbers
        print(i)

# In another loop, all divisors of all numbers in the stop_range
for i in range(stop_range):
    if not is_prime(i):
        divisors = 0
        for j in range(1, i+1):
            if i%j==0:
                divisors+=1
    else:
        divisors = 2
    # If the number of divisors is equal to num_divisors, then print that number
    if divisors == num_divisors:
        print(i)
