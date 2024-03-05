def divide_safe(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        print(round(num1/num2, 5))
    except:
        print(None)

num1 = input()
num2 = input()
divide_safe(num1, num2)