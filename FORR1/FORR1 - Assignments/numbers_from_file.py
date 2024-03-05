def extract_nums(file):
    """Extract all numbers from a file and return them in a sorted list"""
    nums_in_file = []
    for line in file:
        for word in line.split():
            if word.isnumeric():
                nums_in_file.append(int(word))
    
    nums_in_file = sorted(nums_in_file)
    return nums_in_file

legal_name = False

while not legal_name:
    file_name = input()
    try:
        file = open(file_name)
        legal_name = True
    except:
        print(f"{file_name} not found! Please try again.")

print(extract_nums(file))