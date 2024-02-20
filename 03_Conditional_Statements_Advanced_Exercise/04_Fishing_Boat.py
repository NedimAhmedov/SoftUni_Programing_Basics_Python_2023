group_budget = int(input())
season = input()
number_of_fishermen = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer":
    boat_rent = 4200
elif season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

discount = 0

if number_of_fishermen <= 6:
    discount = 0.10
elif 7 <= number_of_fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

extra_discount = 0

if season != "Autumn" and number_of_fishermen % 2 == 0:
    extra_discount = 0.05
else:
    pass

sum = boat_rent * (1 - discount) * (1 - extra_discount)
diff = group_budget - sum

if group_budget >= sum:
    print(f"Yes! You have {diff :.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff) :.2f} leva.")
