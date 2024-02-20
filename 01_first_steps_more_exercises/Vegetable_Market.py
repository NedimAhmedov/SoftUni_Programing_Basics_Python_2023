# •	Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
# •	Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
# •	Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
# •	Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]

kg_price_vegetables = float(input())
fruits_kg = float(input())
vegetables_kg = int(input())
kg_price_fruits = int(input())


total_price_vegetables = kg_price_vegetables * vegetables_kg
total_price_fruits = kg_price_fruits * fruits_kg


sum = total_price_vegetables + total_price_fruits
print(f"{sum/1.94:.2f}")

