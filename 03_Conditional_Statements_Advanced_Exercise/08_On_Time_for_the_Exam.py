exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time_as_min = exam_hour * 60 + exam_min  # трябва да се работи в една мерна единица (по-малката)
arrival_time_as_min = arrival_hour * 60 + arrival_min

diff = arrival_time_as_min - exam_time_as_min
if diff > 0:
    print("Late")
    if diff < 60: # по-мялко от 60 мин
        print(f"{diff} minutes after the start")
    else:
        hh = diff // 60 # часовете в мин.
        mm = diff % 60
        print(f"{hh}:{mm :02d} hours after the start")
elif diff >= -30:  # от пристигането вадим часа [-30 - 0.0]
    print("On time")
    if not diff == 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm :02d} hours before the start")

