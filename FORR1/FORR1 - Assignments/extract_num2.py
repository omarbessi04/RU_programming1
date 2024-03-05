def extract_first_number_from_string(string_to_search):
    split_string = string_to_search.split()
    final = ""
    previous_is_num = False

    for word in split_string:
        if word.isnumeric():
            return(int(word))

        for letter in string_to_search:
            if letter.isnumeric():
                final += letter
                previous_is_num = True
            if (not letter.isnumeric()) and previous_is_num:
                return(int(final))
    
    if final != "":
        return(int(final))
    
    return(-1)