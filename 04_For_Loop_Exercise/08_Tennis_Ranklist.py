import math

tournaments_count = int(input())
starting_point = int(input())

won_points = 0
won_tournament = 0

for _ in range(tournaments_count):
    ranklist = input()
    if ranklist == "W":
        won_points += 2000
        won_tournament += 1
    elif ranklist == "F":
        won_points += 1200
    elif ranklist == "SF":
        won_points += 720

final_points = won_points + starting_point
average_point = won_points / tournaments_count
won_tournament_percent = won_tournament / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_point)}")
print(f"{won_tournament_percent :.2f}%")
