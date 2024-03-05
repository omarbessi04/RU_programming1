def get_function_info(function):
    function_name = str(function.__name__)
    function_description = str(function.__doc__)
    return(f"""Name: {function_name}
    ----------------------------------------
    {function_description}""")