weight_in_kg = float(input())
service_type = input()
distance_in_km = int(input())

price_per_km = 0
express_service_markup = 0
if service_type == "standard":
    if weight_in_kg < 1:
        price_per_km = 0.03
    elif weight_in_kg < 10:
        price_per_km = 0.05
    elif weight_in_kg < 40:
        price_per_km = 0.1
    elif weight_in_kg < 90:
        price_per_km = 0.15
    elif weight_in_kg < 150:
        price_per_km = 0.2

    price_standard = distance_in_km * price_per_km
    print(f"The delivery of your shipment with weight of {weight_in_kg :.3f} kg. would cost {price_standard :.2f} lv.")

if service_type == "express":
    if weight_in_kg < 1:
        price_per_km = 0.03
        express_service_markup = 0.03 * 0.8
    elif weight_in_kg < 10:
        price_per_km = 0.05
        express_service_markup = 0.05 * 0.4
    elif weight_in_kg < 40:
        price_per_km = 0.1
        express_service_markup = 0.1 * 0.05
    elif weight_in_kg < 90:
        price_per_km = 0.15
        express_service_markup = 0.15 * 0.02
    elif weight_in_kg < 150:
        price_per_km = 0.2
        express_service_markup = 0.2 * 0.01

    sum_express_service_markup = weight_in_kg * express_service_markup
    sum_sum_express_service_markup = distance_in_km * sum_express_service_markup
    price_express = distance_in_km * price_per_km + sum_sum_express_service_markup
    print(f"The delivery of your shipment with weight of {weight_in_kg :.3f} kg. would cost {price_express :.2f} lv.")