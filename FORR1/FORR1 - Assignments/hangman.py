class Hangman:
    def __init__(self, word: str) -> None:
        self.word = word.upper()
        self.underscoreWords = ["_ " for i in range(len(word))]
        self.incorrect_guesses = 0

    def guess_letter(self, letter: str) -> bool:
        letter = letter.upper()
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    if i != 0:
                        self.underscoreWords[i] = f" {letter} "
                    else:
                        self.underscoreWords[i] = f"{letter} "
            return True
        else:
            self.incorrect_guesses += 1
            return False
        
    def __str__(self) -> str:
        output = f"{''.join(self.underscoreWords)}\nNumber of incorrect guesses: {self.incorrect_guesses}"
        return output