city = input()
sales = float(input())
commission = 0


if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12


if city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 /100
    elif 500 < sales <= 1000:
        commission = 7.5 /100
    elif 1000 < sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13

if city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 /100
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 12 /100
    elif sales > 10000:
        commission = 14.5 /100

if commission == 0:
    print("error")
else:
    print(f"{sales * commission :.2f}")
