stadium_capacity = int(input())
fans_count = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for each_fan in range(fans_count):
    sector = input()
    if sector == "A":
        a_sector += 1
    elif sector == "B":
        b_sector += 1
    elif sector == "V":
        v_sector += 1
    elif sector == "G":
        g_sector += 1

a_sector_percent = (a_sector / fans_count) * 100
b_sector_percent = (b_sector / fans_count) * 100
v_sector_percent = (v_sector / fans_count) * 100
g_sector_percent = (g_sector / fans_count) * 100
fans_count_percent = (fans_count / stadium_capacity) * 100

print(f"{a_sector_percent :.2f}%")
print(f"{b_sector_percent :.2f}%")
print(f"{v_sector_percent :.2f}%")
print(f"{g_sector_percent :.2f}%")
print(f"{fans_count_percent :.2f}%")