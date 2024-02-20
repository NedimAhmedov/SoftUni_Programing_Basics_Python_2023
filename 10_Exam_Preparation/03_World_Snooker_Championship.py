stage_of_championship = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()

price_per_ticket = 0
discounted_price = 0

if stage_of_championship == "Quarter final":
    if ticket_type == "Standard":
        price_per_ticket = 55.50
    if ticket_type == "Premium":
        price_per_ticket = 105.20
    if ticket_type == "VIP":
        price_per_ticket = 118.90
elif stage_of_championship == "Semi final":
    if ticket_type == "Standard":
        price_per_ticket = 75.88
    if ticket_type == "Premium":
        price_per_ticket = 125.22
    if ticket_type == "VIP":
        price_per_ticket = 300.40
elif stage_of_championship == "Final":
    if ticket_type == "Standard":
        price_per_ticket = 110.10
    if ticket_type == "Premium":
        price_per_ticket = 160.66
    if ticket_type == "VIP":
        price_per_ticket = 400

all_ticket_price = ticket_count * price_per_ticket
if all_ticket_price > 4000:
    discounted_price = all_ticket_price * (1 - 0.25)
elif 2500 < all_ticket_price < 4000:
    discounted_price = all_ticket_price * (1 - 0.10)
else:
    discounted_price = all_ticket_price

if trophy_picture == "Y" and all_ticket_price < 4000:
    discounted_price = discounted_price + (ticket_count * 40)
elif trophy_picture == "N":
    pass

print(f"{discounted_price :.2f}")