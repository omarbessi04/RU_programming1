# Tokenize given file

def check_word_for_specified_tokens(word):
    """Check given word for specified tokens. 
    Returns (0, 0, False) if word has no tokens, returns ("word without the token", "the token", True) otherwise"""
    word_contains_tokens = False
    token_in_word = ""
    # Check if the word contains a specified token
    for token in SPECIFIED_TOKENS:
        if token in word:
            word_contains_tokens = True
            token_in_word = token

    if word_contains_tokens:
        # Using the remove function only available to lists, remove the token from the word
        word_as_list = list(word)
        word_as_list.remove(token_in_word)
        word_without_token = "".join(word_as_list)
        return (word_without_token, token_in_word, word_contains_tokens)
    else:
        return (0, 0, word_contains_tokens)

def check_file():
    """Check file for words and tokens"""
    for line in file:
        line = line.split()
        # For every word in the file, add it to the word list
        for word in line:
            words_in_file.append(word)
            # Check if the word contains specified tokens
            word_without_token, token_in_word, word_contains_tokens = check_word_for_specified_tokens(word)

            if word_contains_tokens:
                tokens_in_file.append(word_without_token)
                tokens_in_file.append(token_in_word)
            else:
                tokens_in_file.append(word)

# Try to open given file
try:
    file = open(input())
    run = True
except:
    run = False

# If there is no file to open, then there is no output
if run:
    SPECIFIED_TOKENS = (",", ".", "!", "?")
    tokens_in_file = []
    words_in_file = []

    check_file()

    print(len(words_in_file))
    for word in words_in_file:
        print(word)

    print(len(tokens_in_file))
    for token in tokens_in_file:
        print(token)