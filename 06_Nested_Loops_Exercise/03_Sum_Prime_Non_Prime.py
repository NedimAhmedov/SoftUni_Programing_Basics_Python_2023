sum_prime_number = 0
sum_non_prime_number = 0

command = input()
while command != "stop":
    new_number = int(command)

    if new_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for i in range(2, new_number):
        if (new_number % i) == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime_number += new_number
    else:
        sum_non_prime_number += new_number

    command = input()

print(f"Sum of all prime numbers is: {sum_prime_number}")
print(f"Sum of all non prime numbers is: {sum_non_prime_number}")