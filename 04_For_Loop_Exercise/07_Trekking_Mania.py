groups_count = int(input())
musala_count = 0
monblant_count = 0
kilimanzharo_count = 0
k2_count = 0
everest_count = 0

for _ in range(groups_count):
    people_count = int(input())
    if people_count <= 5:
        musala_count += people_count
    elif people_count <= 12:
        monblant_count += people_count
    elif people_count <= 25:
        kilimanzharo_count += people_count
    elif people_count <= 40:
        k2_count += people_count
    else:
        everest_count += people_count

sum_people = musala_count + monblant_count + kilimanzharo_count + k2_count + everest_count
musala_percent = musala_count / sum_people * 100
monblant_procent = monblant_count / sum_people * 100
kilimanzharo_proccent = kilimanzharo_count / sum_people * 100
k2_procent = k2_count / sum_people * 100
everest_procent = everest_count / sum_people * 100


print(f"{musala_percent :.2f}%")
print(f"{monblant_procent :.2f}%")
print(f"{kilimanzharo_proccent :.2f}%")
print(f"{k2_procent :.2f}%")
print(f"{everest_procent :.2f}%")