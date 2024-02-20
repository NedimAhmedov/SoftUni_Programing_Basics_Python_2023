n = int(input())
sum = 0
for number in range(n):
    new_number = int(input())
    sum += new_number
avg_sum = sum / n
print(f"{avg_sum :.2f}")