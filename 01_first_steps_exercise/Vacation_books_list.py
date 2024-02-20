# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

book_pages = int(input())
pages_hour = int(input())
reading_days = int(input())

entire_book = book_pages / pages_hour
hours_day = entire_book / reading_days

print (int(hours_day))