from collections import deque

N = int(input())
card = deque([i+1 for i in range(N)])

while len(card) > 1:
    card.popleft()
    x = card.popleft()
    card.append(x)

print(card[0])