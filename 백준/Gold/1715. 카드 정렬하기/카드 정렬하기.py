import heapq

N = int(input())
cards = []
for _ in range(N):
    C = int(input())
    heapq.heappush(cards, C)

result = 0
while len(cards) > 1:
    C1, C2 = heapq.heappop(cards), heapq.heappop(cards)
    v = C1 + C2
    result += v
    heapq.heappush(cards, v)

print(result)