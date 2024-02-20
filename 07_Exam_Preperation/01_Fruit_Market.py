strawberries_price = float(input())
banana_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price * 0.6
banana_price = raspberries_price * 0.2

sum = (strawberries_price * strawberries_quantity) + (banana_price * banana_quantity) \
    + (oranges_price * oranges_quantity) + (raspberries_price * raspberries_quantity)

print(f"{sum :.2f}")