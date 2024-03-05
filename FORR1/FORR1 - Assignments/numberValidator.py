def is_float(string_to_test):
    try:
        string_to_test = float(string_to_test)
        return True
    except:
        return False