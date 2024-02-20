# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

# •	Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]

annual_sub = int(input())
BASKETBALL_SHOES = annual_sub * 0.60
BASKETBALL_CLOTHES= BASKETBALL_SHOES * 0.80
BASKETBALL_BALL =  BASKETBALL_CLOTHES * 0.25
BASKETBALL_ACC =  BASKETBALL_BALL * 0.2


sum = annual_sub + BASKETBALL_SHOES + BASKETBALL_CLOTHES + BASKETBALL_BALL + BASKETBALL_ACC
print(sum)