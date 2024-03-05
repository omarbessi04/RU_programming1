def list_to_int_tuple(search_list):
    int_tuple = ()
    for item in search_list:
        try:
            item = int(item)
            int_tuple = int_tuple + (item,)
        except:
            continue

    return(int_tuple)