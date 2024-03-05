emails_and_grades = {}

run = 0

while run != "n":
    email = input()
    grade = float(input())

    if email in emails_and_grades:
        emails_and_grades[email][0] += grade
        emails_and_grades[email][1] += 1
    else:
        emails_and_grades[email] = [grade, 1]
    
    run = input()

sorted_mails = sorted(emails_and_grades)

for mail in sorted_mails:
    average = round(emails_and_grades[mail][0]/emails_and_grades[mail][1], 2)
    print(f"{mail}: {average}")
