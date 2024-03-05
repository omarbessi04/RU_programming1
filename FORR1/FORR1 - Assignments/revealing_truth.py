def list_to_bool_tuple(search_list):
    bool_tuple = ()

    for item in search_list:
        try:
            item = int(item)
        except:
            pass

        item = bool(item)
        bool_tuple = bool_tuple + (item,)

    return(bool_tuple)