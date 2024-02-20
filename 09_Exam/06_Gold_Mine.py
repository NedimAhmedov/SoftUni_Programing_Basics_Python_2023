location_count = int(input())

for locations in range(1, location_count + 1):
    expected_gold_per_day = float(input())
    expected_working_days = int(input())
    earned_gold_sum_days = 0
    for each_day in range(1, expected_working_days + 1):
        earned_gold_per_day = float(input())
        earned_gold_sum_days += earned_gold_per_day
        avg_earned_gold = earned_gold_sum_days / expected_working_days
    if avg_earned_gold >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {avg_earned_gold :.2f}.")
    else:
        diff = expected_gold_per_day - avg_earned_gold
        print(f"You need {diff :.2f} gold.")