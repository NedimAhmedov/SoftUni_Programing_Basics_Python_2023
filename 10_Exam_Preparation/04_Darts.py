player_name = input()

starting_points = 301
successful_shots = 0
missed_shots = 0

command = input()
while command != "Retire":
    field = command
    points = int(input())

    if field == "Single":
        shot_point = points
        if shot_point <= starting_points:
            starting_points -= shot_point
            successful_shots += 1
        else:
            missed_shots += 1
    elif field == "Double":
        shot_point = 2 * points
        if shot_point <= starting_points:
            starting_points -= shot_point
            successful_shots += 1
        else:
            missed_shots += 1
    elif field == "Triple":
        shot_point = 3 * points
        if shot_point <= starting_points:
            starting_points -= shot_point
            successful_shots += 1
        else:
            missed_shots += 1

    if starting_points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break

    command = input()

if command == "Retire":
    print(f"{player_name} retired after {missed_shots} unsuccessful shots.")
