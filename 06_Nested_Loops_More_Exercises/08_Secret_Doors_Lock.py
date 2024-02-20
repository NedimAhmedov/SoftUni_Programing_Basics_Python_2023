a = int(input())
b = int(input())
c = int(input())

for first in range(1, a + 1):
    for second in range(1, b + 1):
        for third in range(1, c + 1):
            if first % 2 == 0 and third % 2 == 0:  # проверка за четност
                if second == 2 or second == 3 or second == 5 or second == 7:  # проверка за прости числа
                    print(f"{first} {second} {third}")

