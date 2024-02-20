x = float(input()) # височината на къщата
y = float(input()) # дължината на страничната стена
h = float(input()) # височината на триъгълната стена на прокрива

stranichna_stena = x * y
window = 1.5 * 1.5
dve_stranici = 2 * stranichna_stena - 2 * window
vhod = 1.2 * 2
zadna_stena = x * x
predna_zadna_obshto = 2 * zadna_stena - vhod

obshta_plosht = dve_stranici + predna_zadna_obshto

green_paint = obshta_plosht / 3.4
print(f"{green_paint :.2f}")

pokriv_pravougalnici = 2 * (x * y)
pokriv_triugalnici = 2 * (x * h / 2)
obshta_plosht_pokriv = pokriv_pravougalnici + pokriv_triugalnici
red_paint = obshta_plosht_pokriv / 4.3
print(f"{red_paint :.2f}")