numbers_count = int(input())

points = 0
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid_number = 0

for each_number in range(numbers_count):
    new_number = int(input())
    if new_number == 0:
        points += 0
        from_0_9 += 1
    elif new_number < 0:
        points = points / 2
        invalid_number += 1
    elif new_number <= 9:
        points += (0.2 * new_number)
        from_0_9 += 1
    elif new_number <= 19:
        points += (0.3 * new_number)
        from_10_19 += 1
    elif new_number <= 29:
        points += (0.4 * new_number)
        from_20_29 += 1
    elif new_number <= 39:
        points += 50
        from_30_39 += 1
    elif new_number <= 50:
        points += 100
        from_40_50 += 1
    elif new_number > 50:
        points = points / 2
        invalid_number += 1

from_0_9_percent = (from_0_9 / numbers_count) * 100
from_10_19_percent = (from_10_19 / numbers_count) * 100
from_20_29_percent = (from_20_29 / numbers_count) * 100
from_30_39_percent = (from_30_39 / numbers_count) * 100
from_40_50_percent = (from_40_50 / numbers_count) * 100
invalid_number_percent = (invalid_number / numbers_count) * 100

print(f"{points :.2f}")
print(f"From 0 to 9: {from_0_9_percent :.2f}%")
print(f"From 10 to 19: {from_10_19_percent :.2f}%")
print(f"From 20 to 29: {from_20_29_percent :.2f}%")
print(f"From 30 to 39: {from_30_39_percent :.2f}%")
print(f"From 40 to 50: {from_40_50_percent :.2f}%")
print(f"Invalid numbers: {invalid_number_percent :.2f}%")
