num1 = input()
num2 = input()

list1 = sorted(list(num1))
list2 = sorted(list(num2))

if list1 == list2:
    print(f"The numbers {num1} and {num2} are permutations of each other.")
else:
    print(f"The numbers {num1} and {num2} are not permutations of each other.")
