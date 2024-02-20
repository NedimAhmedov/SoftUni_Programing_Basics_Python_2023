start = int(input())
final = int(input())

for number in range(start, final +1):
    number_to_string = str(number)  #  Вземане на текущото число като стринг
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")