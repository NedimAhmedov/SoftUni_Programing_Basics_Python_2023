final_sector = input()
firs_sector_rows = int(input())
odd_row_seats = int(input())

seat_counter = 0

for sector_ord in range(65, ord(final_sector) +1):
    sector = chr(sector_ord)
    for row in range(1, firs_sector_rows + 1):
        if row % 2 != 0:
            for column_ord in range(97, (97 + odd_row_seats)):
                column = chr(column_ord)
                print(f"{sector}{row}{column}")
                seat_counter += 1
        elif row % 2 == 0:
            for column_ord in range(97, (97 + odd_row_seats + 2)):
                column = chr(column_ord)
                print(f"{sector}{row}{column}")
                seat_counter += 1
    firs_sector_rows += 1
print(seat_counter)