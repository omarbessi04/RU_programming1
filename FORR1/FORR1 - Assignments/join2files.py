
def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
                      for sub in [lst1, lst2]]

file1 = open(input())
file2 = open(input())

list1 = []
list2 = []

for line in file1:
    list1.append(line)
for line in file2:
    list2.append(line)

print(countList(list1, list2))