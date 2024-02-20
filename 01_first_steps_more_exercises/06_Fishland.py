# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм

skumriq_kg_price = float(input())
caca_kg_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input()) * 7.5

palamud_price = skumriq_kg_price + skumriq_kg_price * 0.6
safrid_price = caca_kg_price + caca_kg_price * 0.8

sum = (palamud_price * palamud_kg) + (safrid_price * safrid_kg) + midi_kg
print(f"{sum :.2f}")




