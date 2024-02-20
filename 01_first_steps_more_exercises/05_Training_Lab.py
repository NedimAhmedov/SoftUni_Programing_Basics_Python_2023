w = float(input()) * 100
h = float(input()) * 100

desk = 70
lost_workplace = 3
koridor = 100
workplace = 120

hall_w = h - koridor

bura_na_red = hall_w // desk

redove = w // workplace

broy_mesta = redove * bura_na_red - lost_workplace
print(broy_mesta)


