sea_trips = int(input())
mountain_trips = int(input())

won_money = 0

command = input()
while command != "Stop":

    if sea_trips > 0:
        if command == "sea":
            won_money += 680
            sea_trips -= 1

    if mountain_trips > 0:
        if command == "mountain":
            won_money += 499
            mountain_trips -= 1


    if sea_trips == 0 and mountain_trips == 0:
        print("Good job! Everything is sold.")
        print(f"Profit: {won_money} leva.")
        break

    command = input()


if command == "Stop":
    if sea_trips == 0 and mountain_trips == 0:
        print(" Good job! Everything is sold.")
    else:
        print(f"Profit: {won_money} leva.")