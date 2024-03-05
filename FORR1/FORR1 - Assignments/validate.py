def get_name():
    repeat = True
    while repeat:
        name_has_letter = False
        valid_name = True
        string = input("What's your name? ")

        for letter in string:
            if not letter.isalpha() and not letter == " ":
                valid_name = False
            if letter.isalpha():
                name_has_letter = True
        
        if not name_has_letter:
            valid_name = False
        if not valid_name:
            print("Please enter a valid name.")
        
        else:
            repeat = False
    return string


def get_age():
    repeat = True

    while repeat:
        original_age = input("How old are you? ")
        valid_age = True

        try:
            age = int(original_age)
        
            if not 0 <= age <= 125:
                print(f"You seriously expect me to believe you are {original_age} years old?")
                valid_age = False
        
        except:
            print("Please enter an integer.")
            valid_age = False

        if valid_age:
            repeat = False

    return original_age

name = get_name()
age = get_age()

print(f"Nice to meet you {name}.")
print(f"Congratulations on your {age} years.")
