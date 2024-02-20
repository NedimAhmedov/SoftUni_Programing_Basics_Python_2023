first_match_result = input()
second_match_result = input()
third_match_result = input()

won_matches = 0
lost_matches = 0
draw_matches = 0

if ord(first_match_result[0]) > ord(first_match_result[2]):
    won_matches += 1
elif ord(first_match_result[0]) < ord(first_match_result[2]):
    lost_matches += 1
else:
    draw_matches += 1
if ord(second_match_result[0]) > ord(second_match_result[2]):
    won_matches += 1
elif ord(second_match_result[0]) < ord(second_match_result[2]):
    lost_matches += 1
else:
    draw_matches += 1
if ord(third_match_result[0]) > ord(third_match_result[2]):
    won_matches += 1
elif ord(third_match_result[0]) < ord(third_match_result[2]):
    lost_matches += 1
else:
    draw_matches += 1

print(f"Team won {won_matches} games.")
print(f"Team lost {lost_matches} games.")
print(f"Drawn games: {draw_matches}")
