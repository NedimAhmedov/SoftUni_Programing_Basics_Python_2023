days = int(input())

sum_rakia_litres = 0
sum_degrees = 0
for each_days in range(1, days + 1):
    rakia_litres = float(input())
    degrees = float(input())

    sum_degrees += rakia_litres * degrees
    sum_rakia_litres += rakia_litres

average_degrees = sum_degrees / sum_rakia_litres
print(f"Liter: {sum_rakia_litres :.2f}")
print(f"Degrees: {average_degrees :.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif average_degrees < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")