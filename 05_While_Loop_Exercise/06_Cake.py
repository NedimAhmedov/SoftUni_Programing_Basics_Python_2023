cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_width * cake_length

command = input()
while command != "STOP":
    taken_pieces = int(command)

    if taken_pieces <= cake_pieces:
        cake_pieces -= taken_pieces
    elif taken_pieces > cake_pieces:
        needed_pieces = taken_pieces - cake_pieces
        print(f"No more cake left! You need {needed_pieces} pieces more.")
        break

    command = input()

if command == "STOP":
    print(f"{cake_pieces} pieces are left.")
