grades = list(map(float, input().split()))
if len(grades) < 3:
    print("At least 3 scores needed!")
else:
    grades = sorted(grades)
    for i in range(3):
        grades.remove(grades[0])

    grade_sum = round(sum(grades), 1)

    print(f"Sum of scores (3 lowest removed): {grade_sum}")