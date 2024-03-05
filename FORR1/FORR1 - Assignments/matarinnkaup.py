def get_recipe():
    name = input()
    number_of_ingredients = int(input())
    ingredient_dict = {}
    for i in range(number_of_ingredients):
        item, number = input().split()
        if item not in recipe_dict:
            ingredient_dict[item] = int(number)

    recipe_dict[name] = ingredient_dict

def scan_over_receipt():
    number_of_items = int(input())

    for i in range(number_of_items):
        item, number = input().split()

        for ingredient in recipe_dict[item]:
            if ingredient in output_dict:
                output_dict[ingredient] += (recipe_dict[item][ingredient] * int(number))
            else:
                output_dict[ingredient] = (recipe_dict[item][ingredient] * int(number))

recipe_dict = {}
recipies, receipts = input().split()
for i in range(int(recipies)):
    get_recipe()

output_dict = {}
for i in range(int(receipts)):
    scan_over_receipt()

sorted_items = sorted(output_dict)
for item in sorted_items:
    print(f"{item} {output_dict[item]}")