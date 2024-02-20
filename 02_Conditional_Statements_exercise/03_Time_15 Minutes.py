current_hour = int(input())
current_minutes = int(input())

current_minutes_plus_15 = current_minutes + 15
if current_minutes_plus_15 >= 60:
    current_minutes_plus_15 -= 60 # current_minute_plus_15 = current_minute_plus_15 - 60
    current_hour += 1

if current_hour == 24:
    current_hour = 0

print(f"{current_hour}:{current_minutes_plus_15 :02d}")


