days_count = int(input())
hours_per_day = int(input())

total_price = 0
days_counter = 0
price_per_day = 0

for each_day in range(1, days_count + 1):
    days_counter += 1
    price_per_day = 0
    for each_hour in range(1, hours_per_day + 1):
        if each_day % 2 == 0 and each_hour % 2 != 0:
            total_price += 2.50
            price_per_day += 2.5
        elif each_day % 2 != 0 and each_hour % 2 == 0:
            total_price += 1.25
            price_per_day += 1.25
        else:
            total_price += 1
            price_per_day += 1
    print(f"Day: {days_counter} - {price_per_day :.2f} leva")
print(f"Total: {total_price :.2f} leva")