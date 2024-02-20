months = int(input())
total_electricity = 0
water = 20
internet = 15
others = 0

for each_month in range(months):
    electricity = float(input())
    total_electricity += electricity
    others += electricity

total_water = 20 * months
total_internet = 15 * months
others_without_percent = (total_electricity + total_water + total_internet)
percent = others_without_percent * 0.2
others = others_without_percent + percent

average = (total_electricity + total_water + total_internet + others) / months

print(f"Electricity: {total_electricity :.2f} lv")
print(f"Water: {total_water :.2f} lv")
print(f"Internet: {total_internet :.2f} lv")
print(f"Other: {others :.2f} lv")
print(f"Average: {average :.2f} lv")