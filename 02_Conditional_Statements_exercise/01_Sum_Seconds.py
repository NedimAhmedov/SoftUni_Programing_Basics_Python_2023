import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time // 60 # 125 / 60 = 2 мин остатък 5 сек
seconds = total_time % 60 # 125 / 60 = 5 сек
#minutes = math.floor(minutes) #Закръгля получената стойност за минутите надолу

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")