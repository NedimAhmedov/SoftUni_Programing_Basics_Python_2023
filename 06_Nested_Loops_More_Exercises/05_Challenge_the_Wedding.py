men_count = int(input())
women_count = int(input())
tables_count = int(input())

busy_tables = 0


for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        busy_tables += 1
        print(f"({men} <-> {women})", end=" ")
        if busy_tables == tables_count:
            break
    if busy_tables == tables_count:
        break
