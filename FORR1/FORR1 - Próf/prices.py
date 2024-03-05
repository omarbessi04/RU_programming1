run = True
number_of_prices = 0
total_price = 0.0
lowest_price = 1001

while run:
    new_price = float(input())

    # Check if program should halt
    if new_price != 0:
        
        number_of_prices += 1
        
        total_price += new_price

        if new_price < lowest_price:
            lowest_price = new_price
    else:
        run = False


print(f"Number of items: {number_of_prices}")

print(f"Total price: {round(total_price, 2)}")

if number_of_prices > 0:
    print(f"Lowest price: {lowest_price}")
