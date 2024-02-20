annual_fee = int(input())

basketball_shoes_price = annual_fee * 0.6
basketball_equipment_price = basketball_shoes_price * 0.8
basketball_ball_price = basketball_equipment_price * 1 / 4
basketball_accessories_price = basketball_ball_price * 1 /5

sum = annual_fee + basketball_shoes_price + basketball_equipment_price + basketball_ball_price + basketball_accessories_price

print(f"{sum :.2f}")