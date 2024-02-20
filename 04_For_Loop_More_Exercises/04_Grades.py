students_count = int(input())

top_students_count = 0
between_4_5_students_count = 0
between_3_4_students_count = 0
poor_students_count = 0
grades_sum = 0

for each_student in range(students_count):
    each_student_grade = float(input())
    if each_student_grade < 3:
        poor_students_count += 1
        grades_sum += each_student_grade
    elif each_student_grade <= 3.99:
        between_3_4_students_count += 1
        grades_sum += each_student_grade
    elif each_student_grade <= 4.99:
        between_4_5_students_count += 1
        grades_sum += each_student_grade
    elif each_student_grade >= 5:
        top_students_count += 1
        grades_sum += each_student_grade

    avg_grades = grades_sum / students_count
    top_students_count_percent = (top_students_count / students_count) * 100
    between_4_5_students_count_percent = (between_4_5_students_count / students_count) * 100
    between_3_4_students_count_percent = (between_3_4_students_count / students_count) * 100
    poor_students_count_percent = (poor_students_count / students_count) * 100

print(f"Top students: {top_students_count_percent :.2f}%")
print(f"Between 4.00 and 4.99: {between_4_5_students_count_percent :.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4_students_count_percent :.2f}%")
print(f"Fail: {poor_students_count_percent :.2f}%")
print(f"Average: {avg_grades :.2f}")

