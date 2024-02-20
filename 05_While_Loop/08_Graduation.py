student_name = input()
sum_grades = 0
current_class = 1
counter_bad_attempt = 0

while current_class <= 12:
    grade = float(input())
    if grade >= 4:
        current_class += 1
        sum_grades += grade
    elif grade < 4:
        counter_bad_attempt += 1
    if counter_bad_attempt == 2:
        print(f"{student_name} has been excluded at {current_class} grade")
        break
else:
    print(f"{student_name} graduated. Average grade: {sum_grades / 12 :.2f}")