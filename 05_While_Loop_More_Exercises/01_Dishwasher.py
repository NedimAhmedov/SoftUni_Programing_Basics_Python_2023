bottle_count = int(input())
detergent_quantity = bottle_count * 750
number_of_fillings = 1
clean_plate = 0
clean_pot = 0

command = input()
while command != "End":
    dishes_count = int(command)

    if number_of_fillings == 3:
        number_of_fillings = 0
        detergent_quantity -= dishes_count * 15
        clean_pot += dishes_count
        number_of_fillings += 1
    else:
        detergent_quantity -= dishes_count * 5
        number_of_fillings += 1
        clean_plate += dishes_count

    if detergent_quantity < 0:
        needed_detergent = -detergent_quantity
        print(f"Not enough detergent, {needed_detergent} ml. more necessary!")
        break

    command = input()

if command == "End":
    print("Detergent was enough!")
    print(f"{clean_plate} dishes and {clean_pot} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")

