total = int(input())
prices = [int(input()) for _ in range(9)]
print(total - sum(prices))