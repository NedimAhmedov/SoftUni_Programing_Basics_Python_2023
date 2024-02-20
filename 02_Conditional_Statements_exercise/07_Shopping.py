peter_budget = float(input())
count_video_card = int(input())
count_processor = int(input())
count_ram_memory = int(input())

price_video_card = count_video_card * 250
price_processor = price_video_card * 0.35
price_ram = price_video_card * 0.1

sum_all = price_video_card + (price_processor * count_processor) + (price_ram * count_ram_memory)

if count_video_card >= count_processor:
    sum_all = sum_all * (1 - 0.15)

if peter_budget >= sum_all:
    print(f"You have {peter_budget - sum_all :.2f} leva left!")
else:
    print(f"Not enough money! You need {sum_all - peter_budget :.2f} leva more!")
