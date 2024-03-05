def open_file():
    """Tries to open a file, returning the opened file if able"""
    file_name = input()
    info_from_file = 0
    try:
        file = open(file_name)
        info_from_file = read_from_file(file)
    except:
        pass

    return info_from_file

def read_from_file(file):
    """Returns a list of tuples with information from the file"""
    year_and_index_tuple_list = []
    
    for line in file:
        year, index = line.split()
        index = float(index)
        year_and_index_tuple = (year, index)
        year_and_index_tuple_list.append(year_and_index_tuple)

    return year_and_index_tuple_list

def get_list_of_years(file):
    """Given a file, return a list of all the years in the file"""
    list_of_years = []

    for tuple in file:
        # Years are (currently) the first 4 letters of the first object in the tuples
        year = tuple[0][0 : 4]
        year = int(year)
        if not(year in list_of_years):
            list_of_years.append(year)

    return list_of_years

def get_indexes(list_of_years, file):
    """Returns a list of lists, each inner list corresponds to a year inside the file and contains all the indexes of that year"""
    list_of_years = get_list_of_years(file)
    indexes_of_all_years = []

    # For each year, create a list of all the indexes from that year, then append that to the larger list.
    for year in list_of_years:
        this_years_indexes = []
        for year_and_index in file:
            if int(year_and_index[0][0 : 4]) == year:
                this_years_indexes.append(year_and_index[1])

        indexes_of_all_years.append(this_years_indexes)

    return indexes_of_all_years

def print_file_info(file_information):
    """Prints all info in a file"""
    for tuple in file_information:
        print(tuple)

def get_first_and_last_index():
    """Returns a list of tuples in (year, first index, second index) format"""
    first_and_last_index_list = []

    # The order of the index list is the same as the list of years,
    # so for each year, check that years first and last item in the index list
    for i in range(len(list_of_years)):
        year_firstIndex_lastIndex = (list_of_years[i], indexes_of_all_years[i][0], indexes_of_all_years[i][-1])
        first_and_last_index_list.append(year_firstIndex_lastIndex)
    
    return first_and_last_index_list

def print_inflation():
    """Calculates and prints the inflation rate of years"""
    year_and_index_list = get_first_and_last_index()

    for year_and_index in year_and_index_list:
        year = year_and_index[0]
        first_index = year_and_index[1]
        last_index = year_and_index[2]

        inflation_rate = ((last_index - first_index) / first_index) * 100
        inflation_rate = round(inflation_rate, INFLATION_ROUNDING_NUMBER)
        year_inflation_tuple = (year, inflation_rate)
        print(year_inflation_tuple)

INFLATION_ROUNDING_NUMBER = 2

info_from_file = open_file()

if info_from_file != 0:

    # Print all the information in the file
    print_file_info(info_from_file)

    # For each year in the file, print that years first and last index
    # These global variables are needed in order to call get_first_and_last_index()
    list_of_years = get_list_of_years(info_from_file)
    indexes_of_all_years = get_indexes(list_of_years, info_from_file)

    first_and_last_index_list = get_first_and_last_index()
    for tuple in first_and_last_index_list:
        print(tuple)
    
    # For each year in the file, print that years percentage inflation
    print_inflation()
