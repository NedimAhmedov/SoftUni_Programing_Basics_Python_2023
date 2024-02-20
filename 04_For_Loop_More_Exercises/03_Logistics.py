cargo_count = int(input())

tonnage_bus = 0
tonnage_truck = 0
tonnage_train = 0

for each_cargo in range(cargo_count):
    each_cargo_tonnage = int(input())
    if each_cargo_tonnage <= 3:
        tonnage_bus += each_cargo_tonnage
    elif each_cargo_tonnage <= 11:
        tonnage_truck += each_cargo_tonnage
    else:
        tonnage_train += each_cargo_tonnage

sum_tonnage = tonnage_bus + tonnage_truck + tonnage_train
avg_tonnage = ((tonnage_bus * 200) + (tonnage_truck * 175) + (tonnage_train * 120)) / sum_tonnage

tonnage_bus_percent = tonnage_bus / sum_tonnage * 100
tonnage_truck_percent = tonnage_truck / sum_tonnage * 100
tonnage_train_percent = tonnage_train / sum_tonnage * 100

print(f"{avg_tonnage :.2f}")
print(f"{tonnage_bus_percent :.2f}%")
print(f"{tonnage_truck_percent :.2f}%")
print(f"{tonnage_train_percent :.2f}%")