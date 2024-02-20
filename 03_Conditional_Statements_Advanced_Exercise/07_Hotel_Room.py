month_of_year = input()
stays = int(input())

price_studio = 0
price_apartment = 0

if month_of_year == "May" or month_of_year == "October":
    price_apartment = 65
    price_studio = 50
    if stays > 14:  #  първо по-голямото защото когато провери за >7 не влиза в другия елиф
        price_studio = price_studio - (price_studio * 0.30)
        price_apartment = price_apartment - (price_apartment * 0.10)
    elif stays > 7:
        price_studio = price_studio - (price_studio * 0.05)

elif month_of_year == "June" or month_of_year == "September":
    price_apartment = 68.70
    price_studio = 75.20
    if stays > 14:
        price_studio = price_studio - (price_studio * 0.20)
        price_apartment = price_apartment - (price_apartment * 0.10)

elif month_of_year == "July" or month_of_year == "August":
    price_apartment = 77
    price_studio = 76
    if stays > 14:
        price_apartment = price_apartment - (price_apartment * 0.10)

sum_studio = stays * price_studio
sum_apartment = stays * price_apartment

print(f"Apartment: {sum_apartment :.2f} lv.")
print(f"Studio: {sum_studio :.2f} lv.")
