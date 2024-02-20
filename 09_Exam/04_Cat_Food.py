cats_count = int(input())
group_1_count = 0
group_2_count = 0
group_3_count = 0
sum_grams = 0

for _ in range(cats_count):
    grams = float(input())
    sum_grams += grams

    if grams < 200:
        group_1_count += 1
    elif grams < 300:
        group_2_count += 1
    elif grams < 400:
        group_3_count += 1

print(f"Group 1: {group_1_count} cats.")
print(f"Group 2: {group_2_count} cats.")
print(f"Group 3: {group_3_count} cats.")
kg_sum = sum_grams / 1000
price_per_day = kg_sum * 12.45
print(f"Price for food per day: {price_per_day :.2f} lv.")