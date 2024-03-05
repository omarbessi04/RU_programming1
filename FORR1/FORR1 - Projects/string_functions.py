# USER INTERFACE FOR DIFFERENT FUNCTIONS

# func 1: collects digits from string
def collect_digits(a_str):
    final = ""
    for letter in a_str:
        if letter.isnumeric():
            final += letter
    if final != "":
        print(int(final))

# func 2: reverses upper/lower case of string
def inverse_case(a_str):
    new_string = ""
    for letter in a_str:
        if letter == letter.lower():
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

# func 3: converts an integer to a hex number
def to_hex (an_int):
    if an_int.isnumeric():
        an_int = int(an_int)
        hex = []

        # calculate what should be changed to hex
        if an_int > 0:
            while an_int > 0:
                remainder = an_int % 16
                divided = an_int // 16

                an_int = divided
                hex.append(remainder)

        # In reverse order, translate the higher decimal numbers to hex
        final_hex = ""
        for num in hex[::-1]:
            if num > 9:
                if num == 10:
                    final_hex += "A"
                elif num == 11:
                    final_hex += "B"
                elif num == 12:
                    final_hex += "C"
                elif num == 13:
                    final_hex += "D"
                elif num == 14:
                    final_hex += "E"
                elif num == 15:
                    final_hex += "F"
            else:
                final_hex += str(num)
        print(final_hex)


QUIT_INPUT = "q"
COLLECT_DIGITS_INPUT = "c"
INVERSE_CASE_INPUT = "i"
TO_HEX_INPUT = "h"

# User interface:
command = 0
while command != QUIT_INPUT:
    command = input()
    if command == COLLECT_DIGITS_INPUT:
        collect_digits(input())
        
    elif command == INVERSE_CASE_INPUT:
        inverse_case(input())
        
    elif command == TO_HEX_INPUT:
        to_hex(input())
