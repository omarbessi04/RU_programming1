length = int(input())
one_fragment = int(length/3)
num_list = sorted(list(map(int, input().split())))

star_wars_order = []
i = -1
for num in num_list:
    i += 1
    if 0<=i<one_fragment:
        star_wars_order.append(str(num_list[i+one_fragment]))

    elif one_fragment<= i < (one_fragment + one_fragment):
        star_wars_order.append(str(num_list[i-one_fragment]))

    else:
        star_wars_order.append(str(num_list[i]))

print(" ".join(star_wars_order))