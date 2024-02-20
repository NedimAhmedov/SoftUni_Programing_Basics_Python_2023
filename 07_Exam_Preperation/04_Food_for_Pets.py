days = int(input())
total_food = float(input())

food_eaten_by_dog = 0
food_eaten_by_cat = 0
total_biscuits = 0

for each_day in range(1, days + 1):
    current_day_eaten_by_dog = int(input())
    current_day_eaten_by_cat = int(input())
    food_eaten_by_dog += current_day_eaten_by_dog
    food_eaten_by_cat += current_day_eaten_by_cat

    if each_day % 3 == 0:
        total_biscuits += \
            (current_day_eaten_by_dog + current_day_eaten_by_cat) * 0.1

total_food_eaten_by_cat_and_dog = food_eaten_by_dog + food_eaten_by_cat
total_quantity_food_percent = total_food_eaten_by_cat_and_dog / total_food * 100
total_eaten_quantity_by_dog_percent = food_eaten_by_dog / total_food_eaten_by_cat_and_dog * 100
total_eaten_quantity_by_cat_percent = food_eaten_by_cat / total_food_eaten_by_cat_and_dog * 100
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{total_quantity_food_percent :.2f}% of the food has been eaten.")
print(f"{total_eaten_quantity_by_dog_percent :.2f}% eaten from the dog.")
print(f"{total_eaten_quantity_by_cat_percent :.2f}% eaten from the cat.")
