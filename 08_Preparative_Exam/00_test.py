count_dishes = input()
plates = 0
pots = 0
counter = 1
total_detergent = 750 * count_bottles
used_detergent_for_plates = 0
used_detergent_for_pots = 0
used_detergent = 0
count_plates = 0
count_pots = 0

while count_dishes != 'End':
    dishes = int(count_dishes)
    if counter % 3 == 0:
        used_detergent_for_pots = dishes * 15
        total_detergent -= used_detergent_for_pots
        count_pots += dishes
        used_detergent = used_detergent_for_pots
    else:
        used_detergent_for_plates = dishes * 5
        total_detergent -= used_detergent_for_plates
        count_plates += dishes
        used_detergent = used_detergent_for_plates
    if total_detergent < 0:
        print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")

    counter += 1
    count_dishes = input()

print("Detergent was enough!")
print(f"{count_plates} dishes and {count_pots} pots were washed.")
print(f"Leftover detergent {total_detergent} ml.")