def sum_of_divisors(number):
    number = int(number)
    divisor_sum = 0
    for i in range(1, number+1):
        if(number%i==0):
            divisor_sum+=i
    divisor_sum -= number
    return divisor_sum

def decide(number):
    number = int(number)
    thing = sum_of_divisors(number)
    if thing > number:
        return(f"{number} is abundant.")
    elif thing == number:
        return(f"{number} is a perfect number.")
    elif thing < number:
        return(f"{number} is deficient.")
    