savings_per_day = float(input())
won_money_per_day = float(input())
sum_expenses = float(input())
gift_price = float(input())

sum_savings = 5 * savings_per_day
sum_won_money = 5 * won_money_per_day
sum_savings_and_won_money = sum_savings + sum_won_money
sum_savings_and_won_money_minus_expenses = sum_savings_and_won_money - sum_expenses

if sum_savings_and_won_money_minus_expenses >= gift_price:
    print(f"Profit: {sum_savings_and_won_money_minus_expenses :.2f} BGN, the gift has been purchased.")
else:
    diff = gift_price - sum_savings_and_won_money_minus_expenses
    print(f"Insufficient money: {abs(diff) :.2f} BGN.")