entire_string = list(input())
find_letter = input()

index = -1
for letter in entire_string:  
    index+=1
    if letter == find_letter:
        print(index)