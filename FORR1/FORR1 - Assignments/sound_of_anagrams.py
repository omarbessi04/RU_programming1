import string

def make_pretty(sentence_list):
    letters_in_sentence = []
    for word in sentence_list:
        if word != " ":
            word.strip(string.punctuation)
            for letter in word:
                letters_in_sentence.append(letter.lower())

    return letters_in_sentence

words1 = input()
words2 = input()
sentence1 = sorted(make_pretty(words1.split()))
sentence2 = sorted(make_pretty(words2.split()))

if sentence1 == sentence2:
    print(f"{words1} is an anagram of {words2}.")
else:
    print(f"{words1} is not an anagram of {words2}.")
