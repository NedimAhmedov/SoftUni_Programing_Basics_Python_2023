month_of_year = input()
stays = int(input())

price_studio = 0
price_apartment = 0

if month_of_year == "May" or month_of_year == "October":
    price_apartment = 65 * stays
    price_studio = 50 * stays

elif month_of_year == "June" or month_of_year == "September":
    price_apartment = 68.70 * stays
    price_studio = 75.20 * stays

elif month_of_year == "July" or month_of_year == "August":
    price_apartment = 77 * stays
    price_studio = 76 * stays

if stays > 14 and (month_of_year == "May" or month_of_year == "October"):
    price_studio = price_studio * 0.70
elif stays > 7 and (month_of_year == "May" or month_of_year == "October"):
    price_studio = price_studio * 0.95
elif stays > 14 and (month_of_year == "June" or month_of_year == "September"):
    price_studio = price_studio * 0.80

if stays > 14:
    price_apartment = price_apartment * 0.90

print(f"Apartment: {price_apartment :.2f} lv.")
print(f"Studio: {price_studio :.2f} lv.")
