invalid_words_list = []
valid_word_list = []

word = 0
while word != "x":
    word = input().lower()

    if word != "x":
        if valid_word_list == []:
            valid_word_list.append(word)
        
        elif valid_word_list[-1][-1] == word[0]:
            valid_word_list.append(word)
        
        else:
            invalid_words_list.append(word)

print(" ".join(valid_word_list))
print(" ".join(invalid_words_list))
