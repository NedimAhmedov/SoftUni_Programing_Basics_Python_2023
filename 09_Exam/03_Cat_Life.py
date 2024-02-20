breeds_of_cat = input()
gender = input()

years_of_life = 0

if breeds_of_cat == "British Shorthair":
    if gender == "m":
        years_of_life = 13
    elif gender == "f":
        years_of_life = 14
elif breeds_of_cat == "Siamese":
    if gender == "m":
        years_of_life = 15
    elif gender == "f":
        years_of_life = 16
elif breeds_of_cat == "Persian":
    if gender == "m":
        years_of_life = 14
    elif gender == "f":
        years_of_life = 15
elif breeds_of_cat == "Ragdoll":
    if gender == "m":
        years_of_life = 16
    elif gender == "f":
        years_of_life = 17
elif breeds_of_cat == "American Shorthair":
    if gender == "m":
        years_of_life = 12
    elif gender == "f":
        years_of_life = 13
elif breeds_of_cat == "Siberian":
    if gender == "m":
        years_of_life = 11
    elif gender == "f":
        years_of_life = 12
else:
    print(f"{breeds_of_cat} is invalid cat!")
    exit(0)

years_of_life_in_months_human_years = years_of_life * 12
years_of_life_in_months_cats_years = years_of_life_in_months_human_years / 6

print(f"{round(years_of_life_in_months_cats_years)} cat months")