width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height


command = input()
while command != "Done":
    box_size = int(command)
    free_space -= box_size

    if free_space <= 0:
        break

    command = input()

if command == "Done":
    print(f"{free_space} Cubic meters left.")
else:
    needed_space = -free_space
    print(f"No more free space! You need {needed_space} Cubic meters more.")

