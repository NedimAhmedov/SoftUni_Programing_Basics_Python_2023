days = int(input())
type_stay = input()  # "room for one person", "apartment" или "president apartment"
evaluation = input()  # "positive"  или "negative"

nights = days - 1
cost_per_day = 0
discount = 0

if nights < 10:
    if type_stay == "room for one person":
        cost_per_day = 18
    elif type_stay == "apartment":
        cost_per_day = 25
        discount = 0.30
    elif type_stay == "president apartment":
        cost_per_day = 35
        discount = 0.10
if 10 < nights < 15:
    if type_stay == "room for one person":
        cost_per_day = 18
    elif type_stay == "apartment":
        cost_per_day = 25
        discount = 0.35
    elif type_stay == "president apartment":
        cost_per_day = 35
        discount = 0.15
if nights > 15:
    if type_stay == "room for one person":
        cost_per_day = 18
    elif type_stay == "apartment":
        cost_per_day = 25
        discount = 0.50
    elif type_stay == "president apartment":
        cost_per_day = 35
        discount = 0.20

sum = cost_per_day * nights
discounted_price = sum - (sum * discount)
last_price = 0

if evaluation == "positive":
   last_price = discounted_price + (discounted_price * 0.25)
elif evaluation == "negative":
    last_price = discounted_price - (discounted_price * 0.1)

print(f"{last_price :.2f}")