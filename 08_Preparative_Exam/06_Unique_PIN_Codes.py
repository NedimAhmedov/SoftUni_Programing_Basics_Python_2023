# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# for one in range(1, first_number + 1):
#     if one % 2 != 0:
#         continue
#     for two in range (1, second_number + 1):
#         for third in range(1, third_number + 1):
#             if third % 2 != 0:
#                 continue
#             if two == 2 or two == 3 or two == 5 or two == 7:
#                 print(f"{one}{two}{third}")


first_number = int(input())
second_number = int(input())
third_number = int(input())

for first in range(1, first_number + 1):
    if first % 2 != 0:
        continue
    for second in range(2, second_number + 1):
        is_prime = True
        for n in range(2, second):
            if second % n == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        for third in range(1, third_number + 1):
            if third % 2 != 0:
                continue
            print(f"{first} {second} {third}")
