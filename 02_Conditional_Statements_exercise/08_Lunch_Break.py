import math

serial_name = input()
episode_duration = int(input())
brake_duration = int(input())

lunch = brake_duration * 1/8
relax = brake_duration * 1/4
left_brake = brake_duration - lunch - relax

if left_brake >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(left_brake - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(episode_duration - left_brake)} more minutes.")