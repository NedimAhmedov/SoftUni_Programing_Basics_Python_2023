# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
#
# •	Брой пакети химикали - цяло число в интервала [0...100]
# •	Брой пакети маркери - цяло число в интервала [0...100]
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# •	Процент намаление - цяло число в интервала [0...100]
#

pen_pack = int(input()) *5.8
marker_pack = int(input()) *7.2
detergent_liters = int(input()) *1.2
dicount = int(input()) /100

price = (pen_pack +marker_pack + detergent_liters)
discounted_price = price - price * dicount

print(discounted_price)



