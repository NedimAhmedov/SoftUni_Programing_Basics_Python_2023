weather = float(input())

if weather >= 26.00:
    print("Hot")
elif weather >= 20.1:
    print("Warm")
elif weather >= 15.00:
    print("Mild")
elif weather >= 12.00:
    print("Cool")
elif weather >= 5.00:
    print("Cold")
else:
    print("unknown")