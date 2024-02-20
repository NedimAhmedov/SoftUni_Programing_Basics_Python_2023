first_person_eggs = int(input())
second_person_eggs = int(input())

command = input()
while command != "End":

    if command == "one":
        second_person_eggs -= 1
    elif command == "two":
        first_person_eggs -= 1

    if first_person_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_person_eggs} eggs left.")
        break
    elif second_person_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_person_eggs} eggs left.")
        break


    command = input()
if command == "End":
    print(f"Player one has {first_person_eggs} eggs left.")
    print(f"Player two has {second_person_eggs} eggs left.")