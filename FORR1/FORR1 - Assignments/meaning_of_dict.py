#read line into dictionary
def read_into_dict():
    word = input()
    definition = input()
    Siggi_dictionary[word] = definition

Siggi_dictionary = {}
answer = 0

while answer != "n":
    read_into_dict()
    answer = input()

list_of_words = sorted(Siggi_dictionary)

for word in list_of_words:
    print("")
    print(f"{word}:")
    print("   ", Siggi_dictionary[word])