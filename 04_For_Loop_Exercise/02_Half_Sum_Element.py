import sys

max_num = -sys.maxsize
sum_numbers = 0

num_count = int(input())
for i in range(num_count):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    sum_numbers += current_num

rest_num = sum_numbers - max_num
if max_num == rest_num:
    print('Yes')
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")
