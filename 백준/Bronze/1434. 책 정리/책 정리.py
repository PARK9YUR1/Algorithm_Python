N, M = map(int, input().split())  # 박스개수, 책개수
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

idx = 0

for i in range(N):
    while True:
        box = boxes[i]
        if idx == M:
            break
        book = books[idx]

        if box >= book:
            boxes[i] -= book
            idx += 1
        else:
            break

print(sum(boxes))