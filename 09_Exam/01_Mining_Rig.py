import math

price_per_video_card = int(input())
price_per_transition = int(input())
electricity_price_per_card_per_day = float(input())
earning_per_card_per_day = float(input())

sum_video_cards_price = price_per_video_card * 13
sum_transition_price = price_per_transition * 13
sum_expenses = sum_video_cards_price + sum_transition_price + 1000

sum_earning_per_day_per_card = earning_per_card_per_day - electricity_price_per_card_per_day
sum_earning_per_day_sum_cards = 13 * sum_earning_per_day_per_card

return_day = sum_expenses / sum_earning_per_day_sum_cards

print(sum_expenses)
print(math.ceil(return_day))  #  round UP a number