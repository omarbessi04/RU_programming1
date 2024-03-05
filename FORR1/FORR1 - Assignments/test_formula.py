sequence = [0, 3, 30]

for a in range(3, 7):
    sum = (sequence[a-1] + a*3*5) * sequence[a-2]
    sequence.append(sum)
print("sequence1:", sequence)

sequence = [0, 3, 30]
for b in range(3, 7):
    sum = b * (sequence[b-1] + b*15) + 3**b
    sequence.append(sum)

print("sequence2", sequence)


