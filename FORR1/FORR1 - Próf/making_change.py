# Find change only using intergers

available_dollars = [20, 10, 5, 2, 1]

price_of_item = int(input())
amount_paid = int(input())

total_change = amount_paid - price_of_item


while total_change > 0:
    # Check for the highest dollar value we can remove from the total change
    for money in available_dollars:
        if money <= total_change:
            print(money)
            total_change -= money
            # If the highest dollar value has been found, we want to check if we can remove it again - 
            # by starting the loop again instead of going to the next biggest dollar value.
            break
