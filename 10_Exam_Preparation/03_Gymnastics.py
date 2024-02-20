county = input()
sport_equipment = input()

if county == "Russia":
    if sport_equipment == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif sport_equipment == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif sport_equipment == "rope":
        difficulty = 9.600
        performance = 9.00
elif county == "Bulgaria":
    if sport_equipment == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif sport_equipment == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif sport_equipment == "rope":
        difficulty = 9.500
        performance = 9.400
elif county == "Italy":
    if sport_equipment == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif sport_equipment == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif sport_equipment == "rope":
        difficulty = 9.700
        performance = 9.150

sum_point = difficulty + performance
diff = 20 - sum_point
diff_percent = (diff / 20) * 100
print(f"The team of {county} get {sum_point :.3f} on {sport_equipment}.")
print(f"{diff_percent :.2f}%")