target = int(input())

bar_height = target - 30
successful_jumps = 0
failed_jumps = 0
sum_jumps = 0

command = input()
while failed_jumps < 3:
    new_attempt = int(command)

    if new_attempt > bar_height:
        successful_jumps += 1
        bar_height += 5
        failed_jumps = 0
        sum_jumps += 1
        if successful_jumps == 7:
            break
    elif new_attempt <= bar_height:
        failed_jumps += 1
        sum_jumps += 1
        if failed_jumps == 3:
            break

    command = input()

if failed_jumps >= 3:
    print(f"Tihomir failed at {bar_height}cm after {sum_jumps} jumps.")
elif successful_jumps >= 7:
    print(f"Tihomir succeeded, he jumped over {bar_height - 5}cm after {sum_jumps} jumps.")