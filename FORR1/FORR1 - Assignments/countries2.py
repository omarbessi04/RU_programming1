def open_file():
    file_name = input()
    try:
        file = open(file_name)
        return file
    except:
        print(f"File {file_name} not found!")
        return 0

file = 0
while file == 0:
    file = open_file()

country_dictionary = {}
for country in file:
    country = country.strip()
    if len(country) in country_dictionary:
        country_dictionary[len(country)].append(country)
    else:
        country_dictionary[len(country)] = [country]

answer = 0
while answer != "n":
    num = int(input())
    if num in country_dictionary:
        print(", ".join(country_dictionary[num]))
    else:
        print(f"No country name of length {num} exists.")
    answer = input()
