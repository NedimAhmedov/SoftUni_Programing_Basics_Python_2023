standard_ticket = 0
student_ticket = 0
kids_ticket = 0

command = input()

while command != "Finish":
    movie = command
    total_seats = int(input())

    ticket_bought = 0
    ticket_type = input()
    while ticket_type != "End":
        ticket_bought += 1

        if ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "kid":
            kids_ticket += 1

        if ticket_bought == total_seats:
            break

        ticket_type = input()

    percent_full = ticket_bought / total_seats * 100
    print(f"{movie} - {percent_full :.2f}% full.")

    command = input()

total_tickets = student_ticket + standard_ticket + kids_ticket
print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100 :.2f}% student tickets.")
print(f"{standard_ticket / total_tickets * 100 :.2f}% standard tickets.")
print(f"{kids_ticket / total_tickets * 100 :.2f}% kids tickets.")