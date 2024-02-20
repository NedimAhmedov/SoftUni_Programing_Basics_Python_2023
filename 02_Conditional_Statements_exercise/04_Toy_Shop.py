# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

puzzel = 2.6
dol = 3
bear = 4.1
minion = 8.2
truck = 2

trip_price = float(input())
puzzel_count = int(input())
dol_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_money = puzzel_count * puzzel + dol_count * dol + bear_count * bear + minion_count * minion + truck_count * truck
total_toys = puzzel_count + dol_count + bear_count + minion_count + truck_count

if total_toys >= 50:
    total_money = total_money * (1 - 0.25)

total_money = total_money * (1 - 0.1) #rent 10% of all money


if total_money >= trip_price:
    print(f"Yes! {total_money - trip_price :.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_money :.2f} lv needed.")
