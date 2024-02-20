target_money = int(input())

sum_transaction_amount = 0
sum_cash_transaction = 0
sum_card_transaction = 0
cash_transaction_counter = 0
card_transaction_counter = 0

transaction_counter = 0
command = input()
while command != "End":
    transaction_amount = int(command)
    transaction_counter += 1

    if transaction_counter % 2 == 0:
        if transaction_amount >= 10:
            sum_card_transaction += transaction_amount
            sum_transaction_amount += transaction_amount
            card_transaction_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if transaction_amount <= 100:
            sum_cash_transaction += transaction_amount
            sum_transaction_amount += transaction_amount
            cash_transaction_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")

    if sum_transaction_amount >= target_money:
        average_cash_payment = sum_cash_transaction / cash_transaction_counter
        print(f"Average CS: {average_cash_payment :.2f}")
        average_card_payment = sum_card_transaction / card_transaction_counter
        print(f"Average CC: {average_card_payment :.2f}")
        break

    command = input()

if command == "End":
    print("Failed to collect required money for charity.")