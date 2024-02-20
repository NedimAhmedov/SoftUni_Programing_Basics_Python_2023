one_lv_monet_count = int(input())
two_lv_monet_count = int(input())
five_lv_count = int(input())
total_amount = int(input())

for one_lv_count in range(one_lv_monet_count + 1):
    for two_lv_count in range(two_lv_monet_count + 1):
        for five_lv in range(five_lv_count + 1):
            if (one_lv_count * 1) + (two_lv_count * 2) + (five_lv * 5) == total_amount:
                print(f"{one_lv_count} * 1 lv. + {two_lv_count} * 2 lv. + "
                      f"{five_lv} * 5 lv. = {total_amount} lv.")
