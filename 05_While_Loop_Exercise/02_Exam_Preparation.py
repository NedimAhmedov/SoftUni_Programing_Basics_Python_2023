allowed_bad_grades_count = int(input())
sum_problems = 0
all_problems = 0
bad_grades_count = 0
last_problem = ""
has_failed = False



command = input()
while command != "Enough":
    problem_name = command
    grade = int(input())

    all_problems += 1
    sum_problems += grade
    last_problem = problem_name

    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == allowed_bad_grades_count:
            has_failed = True
            break


    command = input()
if not has_failed:
    avg_score = sum_problems / all_problems
    print(f"Average score: {avg_score :.2f}")
    print(f"Number of problems: {all_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades_count} poor grades.")