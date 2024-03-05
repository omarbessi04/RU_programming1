toktik_dictionary = {}

for i in range(int(input())):
    person, views = input().split()
    views = int(views)

    if person in toktik_dictionary:
        toktik_dictionary[person] += views
    else:
        toktik_dictionary[person] = views
    
toktik_values = list(toktik_dictionary.values())
toktik_keys = list(toktik_dictionary.keys())
index = toktik_values.index(max(toktik_values))

print(toktik_keys[index])