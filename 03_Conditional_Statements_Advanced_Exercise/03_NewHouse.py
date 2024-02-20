# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flowers_type = input()
quantity_flowers = int(input())
budget = int(input())

price = 0
discount = 0

if flowers_type == "Roses":
    price = 5
    if quantity_flowers > 80:
        discount = 0.10
elif flowers_type == "Dahlias":
    price = 3.80
    if quantity_flowers > 90:
        discount = 0.15
elif flowers_type == "Tulips":
    price = 2.8
    if quantity_flowers > 80:
        discount = 0.15
elif flowers_type == "Narcissus":
    price = 3.0
    if quantity_flowers < 120:
        discount = - 0.15 #  цената се оскъпява с 15% (отрицателно намаление)
elif flowers_type == "Gladiolus":
    price = 2.5
    if quantity_flowers < 80:
        discount = - 0.20

sum = price * quantity_flowers * (1 - discount)  # формула за смятане на discount

if budget >= sum:
    money_extra = budget - sum
    print(f"Hey, you have a great garden with {quantity_flowers} {flowers_type} and {money_extra:.2f} leva left.")
else:
    money_not_enought = sum - budget
    print(f"Not enough money, you need {money_not_enought :.2f} leva more.")