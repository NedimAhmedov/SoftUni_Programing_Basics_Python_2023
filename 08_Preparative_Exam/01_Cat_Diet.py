fats_percent = int(input())
proteins_percent = int(input())
carbohydrates_percent = int(input())
total_calories = int(input())
water_percent = int(input())

fats_grams = (total_calories * fats_percent) / 9
protein_grams = (total_calories * proteins_percent) / 4
carbohydrates_grams = (total_calories * carbohydrates_percent) / 4
sum_food_grams = fats_grams + protein_grams + carbohydrates_grams
calories_per_gram = total_calories / sum_food_grams

calories_without_water = 100 - water_percent
calories_per_gram_without_water = calories_per_gram * calories_without_water

print(f"{calories_per_gram_without_water :.4f}")
