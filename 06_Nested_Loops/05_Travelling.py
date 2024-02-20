destination = input()

while destination != "End":
    budget = float(input())
    current_money = 0
    while current_money < budget:
        saving = float(input())
        current_money += saving
    print(f"Going to {destination}!")
    destination = input()