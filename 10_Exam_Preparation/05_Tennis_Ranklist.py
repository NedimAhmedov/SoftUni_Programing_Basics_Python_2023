import math

tournaments_count = int(input())
starting_points = int(input())

won_tournaments = 0
final_points = starting_points

for each_tournament in range(1, tournaments_count + 1):
    rank = input()

    if rank == "W":
        final_points += 2000
        won_tournaments += 1
    elif rank == "F":
        final_points += 1200
    elif rank == "SF":
        final_points += 720

avg_points = (final_points - starting_points) / tournaments_count
won_tournaments_percent = won_tournaments / tournaments_count * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{won_tournaments_percent :.2f}%")
