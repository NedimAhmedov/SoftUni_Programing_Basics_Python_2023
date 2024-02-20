budget = float(input())
extras = int(input())
clothing_for_extras = float(input())

decor = budget * 0.1
if extras > 150:
    clothing_for_extras = clothing_for_extras * 0.90

money_needed = decor + extras * clothing_for_extras

if budget >= money_needed:
    print("Action!")
    print(f"Wingard starts filming with {budget - money_needed :.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_needed - budget :.2f} leva more.")
