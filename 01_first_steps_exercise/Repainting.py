# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър

# още 10% от количеството боя
# 2 кв.м. найлон,
# 0.40 лв. за торбички
# заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.

# Входът се чете от конзолата и съдържа точно 4 реда:
# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]


NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
PAINT_THINNER_PRICE = 5
BAG_PRICE = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hour_needed = int(input())

nylon_extra_quantity = 2
paint_extra_quantity = 0.10 * paint_quantity

total_material_price = (nylon_quantity + nylon_extra_quantity) * NYLON_PRICE \
                       + (paint_quantity + paint_extra_quantity) * PAINT_PRICE \
    + paint_thinner_quantity * PAINT_THINNER_PRICE \
    + BAG_PRICE

work_per_hours_price = total_material_price * 0.30

total_price = total_material_price + work_per_hours_price * work_hour_needed

print(total_price)



