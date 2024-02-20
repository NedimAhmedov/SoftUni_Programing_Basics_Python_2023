first_letter = input()
second_letter = input()
third_letter = input()

combinations_counter = 0

for first in range(ord(first_letter), ord(second_letter) + 1):  #  return the integer that represents the character
    if first == ord(third_letter):
        continue
    for second in range(ord(first_letter), ord(second_letter) + 1):
        if second == ord(third_letter):
            continue
        for third in range(ord(first_letter), ord(second_letter) + 1):
            if third == ord(third_letter):
                continue

            combinations_counter += 1

            print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")  #  Get the character that represents the unicode
print(combinations_counter)

