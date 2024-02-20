starting_points = int(input())

bonus_point = 0

if starting_points <= 100:
    bonus_point = 5
elif 1000 >= starting_points > 100:  # 100 - 1000
    bonus_point = starting_points * 0.20
else:
    bonus_point = starting_points * 0.10


if starting_points % 2 == 0:
   bonus_point += 1  # bonus = bonus + 1
elif starting_points % 10 == 5:
   bonus_point = bonus_point + 2

print(bonus_point)
print(bonus_point + starting_points)
