won_matches = 0
lost_matches = 0

command = input()
while command != "End of tournaments":
    tournament_name = command
    game_count = int(input())
    game_counter = 0
    for each_game in range(game_count):
        first_team_score = int(input())
        second_team_score = int(input())
        game_counter += 1

        if first_team_score > second_team_score:
            diff = first_team_score - second_team_score
            print(f"Game {game_counter} of tournament {tournament_name}: win with {diff} points.")
            won_matches += 1
        elif second_team_score > first_team_score:
            diff = second_team_score - first_team_score
            print(f"Game {game_counter} of tournament {tournament_name}: lost with {diff} points.")
            lost_matches += 1
    command = input()
if command == "End of tournaments":
    wons_perc = won_matches / (won_matches + lost_matches) * 100
    print(f"{wons_perc :.2f}% matches win")
    lost_perc = lost_matches / (won_matches + lost_matches) * 100
    print(f"{lost_perc :.2f}% matches lost")