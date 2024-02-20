# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.

# десерт, чиято цена е равна на 20% от общата сметка (без доставката).

# Цената на доставка е 2.50

CHIKEN_MENU = 10.35
FISH_MENU = 12.40
VEGI_MENU = 8.15
DESERT = 0.20
DELIVERY = 2.50

chiken_menu_number = int(input())
fish_menu_number = int(input())
vegi_menu_number = int(input())

sum_all_menu = chiken_menu_number*CHIKEN_MENU + fish_menu_number*FISH_MENU + vegi_menu_number*VEGI_MENU
desert_price = sum_all_menu * DESERT
final_price = sum_all_menu + desert_price + DELIVERY

#print(sum_all_menu)
#print(desert_price)
print(final_price)

