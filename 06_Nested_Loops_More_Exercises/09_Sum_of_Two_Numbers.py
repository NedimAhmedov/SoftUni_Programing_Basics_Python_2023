start = int(input())
end = int(input())
magic_number = int(input())

combination_counter = 0
magic_number_found = False

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            magic_number_found = True
            print(f"Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})")
            break
    if magic_number_found:
        break

if not magic_number_found:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
