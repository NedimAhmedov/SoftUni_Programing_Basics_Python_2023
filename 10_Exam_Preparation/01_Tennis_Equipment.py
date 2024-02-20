import math

tennis_racket_price = float(input())
tennis_racket_count = int(input())
pair_of_shoes_count = int(input())

tennis_racket_sum_price = tennis_racket_count * tennis_racket_price
pair_of_shoes_price = tennis_racket_price / 6
shoes_price_sum = pair_of_shoes_count * pair_of_shoes_price
other_equipment_price = (tennis_racket_sum_price + shoes_price_sum) * 0.2
sum_price = tennis_racket_sum_price + shoes_price_sum + other_equipment_price

djokovic_price = sum_price / 8
sponsors_price = sum_price * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")