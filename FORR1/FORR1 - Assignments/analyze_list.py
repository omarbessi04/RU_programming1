def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return True

valid_name = False
while not valid_name:
    try:
        original_list = list(map(int, input().split(",")))
        valid_name = True

        for num in original_list:
            if num < 0:
                valid_name = False

        if not valid_name:
            print("Incorrect input! Please try again.")
    except:
        print("Incorrect input! Please try again.")

sorted_list = sorted(original_list)

bad_composite_list = ["None" if is_prime(num) else num for num in sorted_list]
composite_list = []

for num in bad_composite_list:
    if num != "None" and num not in composite_list:
        composite_list.append(num)

sum = 0
for num in original_list:
    sum += num
average = sum/len(original_list)

print("Input list:", original_list)
print("Sorted list:", sorted_list)
print("Composite list:", composite_list)
print(f"Min: {min(original_list)}, Max: {max(original_list)}, Average: {average:.2f}")