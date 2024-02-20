
cycles = int(input())

oddSum = 0
evenSum = 0
odd_max = -1000000000.0
odd_min = 1000000000.0
even_max = -1000000000.0
even_min = 1000000000.0

for i in range(1, cycles + 1):
    num = float(input())
    if i % 2 != 0:
      oddSum += num
      if num > odd_max:
          odd_max = num
      if num < odd_min:
          odd_min = num
    elif i % 2 == 0:
        evenSum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
print(f"OddSum={oddSum :.2f},")
if odd_min != 1000000000.0:
    print(f"OddMin={odd_min :.2f},")
else:
    print("OddMin=No,")
if odd_max != -1000000000.0:
    print(f"OddMax={odd_max :.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={evenSum :.2f},")
if even_min != 1000000000.0:
    print(f"EvenMin={even_min :.2f},")
else:
    print("EvenMin=No,")
if even_max != -1000000000.0:
    print(f"EvenMax={even_max :.2f}")
else:
    print("EvenMax=No")

