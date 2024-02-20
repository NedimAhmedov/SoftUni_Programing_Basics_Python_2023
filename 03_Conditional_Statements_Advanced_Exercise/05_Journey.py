budget = float(input())
season = input()

spent_money = 0
destination = ""
camp_or_hotel = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.3
        camp_or_hotel = "Camp"
    if season == "winter":
        spent_money = budget * 0.7
        camp_or_hotel = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.4
        camp_or_hotel = "Camp"
    if season == "winter":
        spent_money = budget * 0.8
        camp_or_hotel = "Hotel"
else:
    destination = "Europe"
    spent_money = budget * 0.9
    camp_or_hotel = "Hotel"

print(f"Somewhere in {destination}")
print(f"{camp_or_hotel} - {spent_money :.2f}")






