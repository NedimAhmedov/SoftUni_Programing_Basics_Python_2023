bought_food = int(input()) * 1000
sum_eaten_food = 0
command = input()
while command != "Adopted":
    eaten_food_in_grams = int(command)
    sum_eaten_food += eaten_food_in_grams

    command = input()

diff = abs(bought_food - sum_eaten_food)
if command:
    if sum_eaten_food <= bought_food:
        print(f"Food is enough! Leftovers: {round(diff)} grams.")
    else:
        print(f"Food is not enough. You need {round(diff)} grams more.")