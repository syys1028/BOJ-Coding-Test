import sys
input = sys.stdin.readline

N = int(input())
book_count = {}

for _ in range(N):
    title = input().strip()
    if title in book_count:
        book_count[title] += 1
    else:
        book_count[title] = 1

max_count = max(book_count.values())

most_sold_books = [title for title in book_count if book_count[title] == max_count]

most_sold_books.sort()
print(most_sold_books[0])