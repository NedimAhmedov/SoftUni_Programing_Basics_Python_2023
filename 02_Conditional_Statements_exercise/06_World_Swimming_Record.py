record = float(input())
distance_meters = float(input())
second_per_meter = float(input())

ivan_should_swim = distance_meters * second_per_meter
delay = distance_meters // 15 * 12.5

sum_time = ivan_should_swim + delay

if sum_time >= record:
    print(f"No, he failed! He was {sum_time - record :.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")
