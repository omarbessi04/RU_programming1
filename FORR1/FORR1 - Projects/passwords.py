# CHECK IF GIVEN PASSWORDS ARE VALID

run = True
password_attemps = 0
failed_attemps = 0
valid_attemps = 0
MINIMUN_PASS_LENGTH = 6
MAXIMUM_PASS_LENGTH = 20


while run:
    length_check = False
    includes_lowercase = False
    includes_uppercase = False
    includes_numeric = False

    password = input()

    if password == "q":
        run = False
        
    else:
        password_attemps += 1
        # Length check
        if MINIMUN_PASS_LENGTH <= len(password) <= MAXIMUM_PASS_LENGTH:
            length_check = True

            # Lowercase / Uppercase / Numeric check
            for letter in password:

                if letter.isupper():
                    includes_uppercase = True

                if letter.islower():
                    includes_lowercase = True

                if letter.isnumeric():
                    includes_numeric = True

        
        #If all conditions are met, print valid password and it's length
        if length_check and includes_lowercase and includes_uppercase and includes_numeric:
            print(f"{password}: Valid password of length {len(password)}.")
            valid_attemps += 1

        else:
            failed_attemps += 1

            # Print failure statements
            if not MINIMUN_PASS_LENGTH <= len(password) <= MAXIMUM_PASS_LENGTH:
                print(f"{password}: Invalid length.")
                
            else:
                if not includes_lowercase:
                    print(f"{password}: Missing lower case letter.")

                if not includes_uppercase:
                    print(f"{password}: Missing upper case letter.")
                
                if not includes_numeric:
                    print(f"{password}: Missing numeric letter.")

print(f"You tried {password_attemps} passwords, {valid_attemps} valid, {failed_attemps} invalid.")
