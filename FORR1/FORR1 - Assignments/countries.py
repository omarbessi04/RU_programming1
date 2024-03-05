suffix = input().strip()
total = 0
countries = open("countries.txt", "r")
for country in countries:
    country = country.strip()
    if country.endswith(suffix):
        print(country)
        total += 1
print(f"{total} countries with suffix {suffix} in total.")