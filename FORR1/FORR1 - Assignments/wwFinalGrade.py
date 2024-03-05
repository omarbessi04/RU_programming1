def get_data() -> list[str] | None:
    """Gets data"""

    filename = input()
    try:
        with open(filename) as file:
            data = file.readlines()
    except FileNotFoundError:
        return None

    return data