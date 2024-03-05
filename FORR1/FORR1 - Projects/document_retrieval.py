import string

def clean_string(word):
    """Clean up given string by lowering and stripping it"""
    word = word.lower()
    word = word.strip()
    word = word.strip(string.punctuation)
    return word

# prompt user for name of text file, if no text file is given, no output is generated
def open_file(file_name):
    """Try to open given file, return 0 if the file couldn't be opened, return the file otherwise"""
    try:
        new_file = open(file_name)
        return new_file
    except:
        return 0

# read document, and store it as a list of strings (one list for each document)
def read_document(file):
    """Read all text from file and put all words from every given document into a list of strings"""
    all_document_data = [[]]
    for line in file:
        # the line "END OF DOCUMENT" states that the current document is over and now a new document appears
        if line.strip().strip(string.punctuation).lower() == "end of document":
            all_document_data.append([])

        else:
            all_document_data[-1].append(line)

    all_document_data.pop()
    return all_document_data

# to keep track of words, have dictionary like this {lowercase word: {documents where the word appears}}
def create_word_dictionary(document_datalist):
    """With given list of lists, create a dictionary where the keys are individual words and values are the documents in which the word appears"""
    word_dict = {}
    # for each list within the list of lists (or, for every document within the list)
    for i in range(len(document_datalist)):
        for line in document_datalist[i]:
            # check every word in that list
            for word in line.split():
                # clean it, and then add it to the dictionary with it as the key and the current document as the value
                word = clean_string(word)
                if word in word_dict:
                    word_dict[word].add(i+1)
                else:
                    word_dict[word] = set({i+1})
    return word_dict

# search, print the number of documents with all matching search queries
def search(search_querie):
    """Search for a given word string in the word dictionary"""
    # check if the search querie is empty or a space, 
    if search_querie == "" or search_querie == " ":
        print("No match")
        return
        
    search_querie = search_querie.split()
    real_search = []
        
        # only do the search if every word in the querie is in the word dictionary
    for word in search_querie:
        word = word.lower()
        if word in word_dictionary:
            real_search.append(word)

    if len(real_search) != len(search_querie) or real_search == []:
        print("No match")
        return
    
    # get the value of each word in the dictionary (this value will be a set)
    final = word_dictionary[real_search[0]]
    for item in real_search:
        # by using "&" we are left with what is in both sets
        final = final & word_dictionary[item]

    # check if this new set is empty
    if final != set():
        final = list(map(str, sorted(final)))
        print(f"Documents matching search: {' '.join(final)}")
    else:
        print("No match")

# print, user is prompted for number of document, print out the entire document
def print_document(document_index):
    """Prints out the entire document at the given document index"""

    # check if the document index isn't a number or is a space
    if not(document_index.isnumeric() and document_index != ""):
        print("No match")
        return
        
    # check if the document index is too high or too low
    document_index = int(document_index)
    if not(1 <= document_index <= len(document_word_list)):
        print("No match")
        return
    
    # if the document index passes those two checks,print
    print(f"Document #{document_index}:")
    print("".join(document_word_list[document_index-1]), end="")

def main():
    """The main function controls the user interface"""
    LEGAL_ANSWERS = ["search", "print"]
    answer = "search"
    while answer in LEGAL_ANSWERS:
        answer = input()
        if answer == "print":
            print_document(input())
        elif answer == "search":
            search(input())

file = open_file(input())
# if the file can be opened, create everything needed for the main function, then run the main function
if file != 0:
    document_word_list = read_document(file)
    word_dictionary = (create_word_dictionary(document_word_list))
    main()