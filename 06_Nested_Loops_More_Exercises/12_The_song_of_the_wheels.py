control_number_m = int(input())

numbers_counter = 0
fourth_password = ""
password_list = []

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b and c > d and control_number_m == (a * b) + (c * d):
                    current_password = f"{a}{b}{c}{d}"
                    password_list.append(current_password)
                    numbers_counter += 1
                    if numbers_counter == 4:
                        fourth_password = f"Password: {a}{b}{c}{d}"
print(" ". join(password_list))
if fourth_password != "":
    print(fourth_password)
else:
    print("No!")