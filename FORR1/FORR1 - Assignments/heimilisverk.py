my_set = set({})
for i in range(int(input())):
    chore = input()
    if not (chore in my_set):
        print(chore)
        my_set.add(chore)
