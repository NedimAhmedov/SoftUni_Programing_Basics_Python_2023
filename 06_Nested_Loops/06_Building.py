ground = int(input())
rooms = int(input())

for grounds_in_building in range(ground, 0, -1):  # принтваме в нисходящ ред
    for rooms_on_ground in range(rooms):
        if grounds_in_building == ground:
            print(f"L{grounds_in_building}{rooms_on_ground}", end=" ")
        elif grounds_in_building % 2 == 0:
            print(f"O{grounds_in_building}{rooms_on_ground}", end=" ")
        else:
            print(f"A{grounds_in_building}{rooms_on_ground}", end=" ")

    print()  # преминаваме на нов ред