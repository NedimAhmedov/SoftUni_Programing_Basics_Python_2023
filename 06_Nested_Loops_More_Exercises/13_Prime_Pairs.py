first_numbers_start = int(input())
second_numbers_start = int(input())
start_end_diff_first_numbers = int(input())
start_end_diff_second_numbers = int(input())

for first in range(first_numbers_start, (first_numbers_start + start_end_diff_first_numbers) + 1):
    is_prime = True
    for n in range(2, first):
        if first % n == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    for second in range(second_numbers_start, (second_numbers_start + start_end_diff_second_numbers) + 1):
        is_prime = True
        for n in range(2, second):
            if second % n == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        print(f"{first}{second}")