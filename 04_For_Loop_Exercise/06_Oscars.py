actor = input()
academy_points= float(input())
judge_count = int(input())

total_points = academy_points
for _ in range(judge_count):
    judge_name = input()
    judge_points = float(input())
    actual_point = len(judge_name) * judge_points / 2
    total_points += actual_point
    if total_points > 1250.5:
        break

if total_points <= 1250.5:
    print(f"Sorry, {actor} you need {1250.5 - total_points :.1f} more!")
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!")