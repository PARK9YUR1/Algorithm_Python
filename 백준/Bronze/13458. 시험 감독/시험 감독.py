N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
A = [(a-B if a-B>0 else 0) for a in A]
arr = [a//C + x for a in A for x in [1 if a%C else 0]]
result += sum(arr)

print(result)