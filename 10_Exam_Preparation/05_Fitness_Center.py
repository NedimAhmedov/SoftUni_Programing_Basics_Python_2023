fitness_visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for each_visitor in range(1, fitness_visitors + 1):
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

training_percent = (back + chest + legs + abs) / fitness_visitors
protein_buyers_percent = (protein_shake + protein_bar) / fitness_visitors

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training_percent * 100 :.2f}% - work out")
print(f"{protein_buyers_percent * 100:.2f}% - protein")

