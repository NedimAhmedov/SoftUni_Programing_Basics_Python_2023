family_budget = float(input())
stays = int(input())
price_per_stay = float(input())
percent_extra_expense = int(input()) / 100

if stays > 7:
    price_per_stay -= price_per_stay * 0.05  #  price_per_stay *= 0.95

trip_price = stays * price_per_stay
extra_expenses_amount = family_budget * percent_extra_expense
sum_cost = trip_price + extra_expenses_amount

diff = abs(family_budget - sum_cost)
if family_budget >= sum_cost:
     print(f"Ivanovi will be left with {diff :.2f} leva after vacation.")
else:
    print(f"{diff :.2f} leva needed.")