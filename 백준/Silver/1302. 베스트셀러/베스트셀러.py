N = int(input())
book = {}
for _ in range(N):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

new_book = sorted(book.items(), key=lambda x:(-x[1], x[0]))
print(new_book[0][0])