deposit = input()
sum = 0

while deposit != "NoMoreMoney":
    new_deposit = float(deposit)
    if new_deposit < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {new_deposit :.2f}")
    sum += new_deposit
    deposit = input()
print(f"Total: {sum :.2f}")