import string

def open_file():
    file_name = input()
    try:
        file = open(file_name)
        return file
    except:
        return 0
    
def change_file_to_set(file):
    file_set = set()
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip()
            word = word.strip(string.punctuation)
            file_set.add(word)
    return file_set

def find_common_words():
    return file1 & file2

def find_either_words():
    return file1^file2
    
def find_exclusive_first_words():
    exclusive = file1 - common_words
    return exclusive
    
def print_from_set(setting, file):
    print()
    words = sorted(list(file))
    length = len(words)

    if setting == 0:
        print(f"The two files have {length} words in common.")
        print(sentence)

    elif setting == 1:
        print(f"There are {length} words that are only in either file but not both.")
        print(sentence)

    elif setting == 2:
        print(f"There are {length} words that only appear in the first file.")
        print(sentence)
    
    if length > 1:
        print(", ".join(words[0:-1]) + " and "+ words[-1] + ".")
    else:
        print(*words)

file1 = change_file_to_set(open_file())
file2 = change_file_to_set(open_file())

common_words =find_common_words()
either_words = find_either_words()
exclusive_first_words = find_exclusive_first_words()
sentence = "These words are as follows:"

lst = [common_words, either_words, exclusive_first_words]
for i in range(3):
    print_from_set(i, lst[i])