inherited_money = float(input())
expected_living_year = int(input())

spent_money = 0
age = 18
current_year = 1800
for years in range(current_year, expected_living_year + 1):
    if years % 2 == 0:
        spent_money += 12000
    else:
        spent_money += 12000 + (age * 50)
    age += 1
diff = abs(inherited_money - spent_money)
if spent_money <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {diff :.2f} dollars left." )
else:
    print(f"He will need {diff :.2f} dollars to survive." )