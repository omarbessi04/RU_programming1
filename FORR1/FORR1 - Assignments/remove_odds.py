def extract_evens(int_list):
    """Returns a new list with only even integers from int_list, without modifying int_list."""
    evens_list = []
    for num in int_list:
        if num % 2 == 0:
            evens_list.append(num)

    return evens_list

def remove_odds(int_list):
    """Removes odd integers from int_list, thus modifying int_list."""
    copy_list = int_list[:]
    
    for num in copy_list:
        if num % 2 != 0:
            int_list.remove(num)

    
