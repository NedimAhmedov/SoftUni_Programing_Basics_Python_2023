target_book = input()
books_count = 0
is_found = False

command = input()
while command != "No More Books":
    current_book = command

    if current_book == target_book:
        is_found = True
        break

    books_count += 1
    command = input()

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
else:
    print(f"You checked {books_count} books and found it.")