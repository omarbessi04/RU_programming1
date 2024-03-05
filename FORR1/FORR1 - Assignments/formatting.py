number = float(input())
number = f'{number:.2f}'

to_print = f"{' '*(12 - len(str(number)))}{number}\n"
print(to_print)
