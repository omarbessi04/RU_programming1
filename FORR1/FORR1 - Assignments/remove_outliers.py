def without_outliers(a_list):
    """Returns a new list. Does not modify the list passed as an argument."""
    new_list = a_list[:]
    copy_list = new_list[:]
    
    new_list = sorted(new_list)

    copy_list.remove(new_list[0])
    copy_list.remove(new_list[-1])
    
    return copy_list

def remove_min_and_max(a_list):
    """Returns nothing, modifies the list passed as an argument."""
    new_list = a_list[:]
    new_list = sorted(new_list)
    a_list.remove(new_list[0])
    a_list.remove(new_list[-1])

