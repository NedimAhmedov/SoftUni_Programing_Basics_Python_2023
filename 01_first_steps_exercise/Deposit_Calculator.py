# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit = float(input())
deposit_exp = int(input())
year_interest = float(input()) / 100

sum = deposit + deposit_exp * ((deposit * year_interest) / 12)
print(sum)