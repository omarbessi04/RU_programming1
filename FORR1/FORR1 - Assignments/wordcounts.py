import string
def open_text_file():
    file_name = input()
    try:
        file = open(file_name)
        return file
    except:
        return 0
    
def change_file_to_list():
    word_list = []
    for line in word_file:
        split_lines = line.split()
        for word in split_lines:
            clean_word = word.lower().strip(string.punctuation)
            word_list.append(clean_word)
    change_list_to_dict(word_list)

def change_list_to_dict(word_list):
    for word in word_list:
        occurences_of_word = word_list.count(word)
        if occurences_of_word in word_dict:
            if word not in word_dict[occurences_of_word]:
                word_dict[occurences_of_word].append(word)
        else:
            word_dict[occurences_of_word] = [word]

def print_output():
    reversed_key_dict = sorted(word_dict.keys(), reverse=True)
    for key in reversed_key_dict:
        occurences = len(word_dict[key])

        if occurences == 1 and key == 1:
            print(f"There's only 1 word that appears only once:")
        elif occurences == 1:
            print(f"There's only 1 word that appears {key} times:")
        elif key == 1:
            print(f"There are {occurences} words that appear only once:")
        else:
            print(f"There are {occurences} words that appear {key} times:")
        print(" " + ", ".join(word_dict[key]))

word_dict = {}
word_file = open_text_file()
if word_file != 0:
    change_file_to_list()
    print_output()
    