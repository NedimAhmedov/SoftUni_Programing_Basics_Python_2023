import math

processor_count = int(input())
workers_count = int(input())
working_days = int(input())

sum_working_hours = workers_count * working_days * 8
sum_made_processors = sum_working_hours / 3
sum_made_processors = math.floor(sum_made_processors)
diff = abs(processor_count - sum_made_processors) * 110.10

if sum_made_processors < processor_count:
    print(f"Losses: -> {diff :.2f} BGN")
else:
    print(f"Profit: -> {diff :.2f} BGN")