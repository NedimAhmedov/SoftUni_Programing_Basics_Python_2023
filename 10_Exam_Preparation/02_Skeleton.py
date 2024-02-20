control_minutes = int(input())
control_seconds = int(input())
length_metres = float(input())
seconds_for_hundred_metres = int(input())

control_time = control_minutes * 60 + control_seconds
time_reduction = length_metres / 120
sum_reduced_time = time_reduction * 2.5
marins_time = (length_metres / 100) * seconds_for_hundred_metres - sum_reduced_time

if control_time >= marins_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marins_time :.3f}.")
else:
    diff = control_time - marins_time
    print(f"No, Marin failed! He was {abs(diff) :.3f} second slower.")