def string_to_set(word):
    word_set = set()
    for i in range(len(word)):
        if word[i].isupper():
            if i != len(word)-1:
                if word[i+1].islower():
                    word_set.add((f"{word[i]}{word[i+1]}"))
                else:
                    word_set.add(word[i])
            else:
                word_set.add(word[i])

    return word_set


formula1 = string_to_set(input())
formula2 = string_to_set(input())

shared = sorted(formula1 & formula2)

print(", ".join(shared))