def open_file(file):
    """Try to open given file, return 0 if the file couldn't be opened, return the file otherwise"""
    try:
        new_file = open(file)
        return new_file
    except:
        return 0
    
def find_word(file, index):
    """Returns a word at the given line number in a file"""
    file_list = []
    for line in file:
        file_list.append(line)
    return list(file_list[index-1].strip())

def correct_guess(guess):
    """Prints message and adds the letter to the hidden word list"""
    print(f"Correct letter {guess}!")
    return add_letter_to_hidden_word_list(guess)

def add_letter_to_hidden_word_list(guess):
    """Adds a correctly guessed letter to the hidden word"""
    # Get all instances of letter in word and check index
    index_list = []
    for i in range(len(secret_word_list)):
        if secret_word_list[i] == guess:
            index_list.append(i)

    # Match that index in the hidden word list, and put the guess there
    for index in index_list:
        hidden_word_list[index] = guess
    
    return hidden_word_list

MAXIMUM_TRIES = 12
file = open_file(input())

# If the file couldn't be opened, no output is generated
if file != 0:
    
    # The secret word that will be hidden from the player
    secret_word_list = find_word(file, int(input()))
    # The hidden word that will be shown to the player
    hidden_word_list = ["-" for i in range(len(secret_word_list))]
    hidden_word = " ".join(hidden_word_list)

    current_guess = 0

    # End the game when the player has ran out of guesses or has filled out the word list
    while (current_guess < MAXIMUM_TRIES) and (secret_word_list != hidden_word_list):
        current_guess += 1

        print(f"Secret word: {hidden_word}")
        print(f"Guess {current_guess}/{MAXIMUM_TRIES}")

        letter = input()
        if letter in secret_word_list:
            # If the guess is correct, add it to the hidden word list and update the hidden word
            hidden_word_list = correct_guess(letter)
            hidden_word = " ".join(hidden_word_list)
        else:
            print(f"Incorrect letter {letter}!")
    
    # When the game is over, print relevant messages
    print(f"Secret word: {hidden_word}")
    if secret_word_list == hidden_word_list:
        print("You won!")
    else:
        secret_word = "".join(secret_word_list)
        print(f"You lost! The secret word was {secret_word}")