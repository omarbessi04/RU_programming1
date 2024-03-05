# Compute a series of a given length

# We only care about the first 10 items in the series, so put them into a list
series = [0.5, 0.75, 0.875, 0.9375, 0.96875, 0.984375, 0.9921875, 0.99609375, 0.998046875, 0.9990234375]

length_of_series = int(input())

for i in range(length_of_series):
    print(series[i])
