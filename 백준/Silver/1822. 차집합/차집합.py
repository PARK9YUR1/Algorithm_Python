import sys
input = sys.stdin.readline

a, b = map(int, input().split())  # A, B 원소개수
A = set(map(int, input().split()))
B = set(map(int, input().split()))

lst = []
for i in A:
    if i not in B:
        lst.append(i)
lst.sort()

print(len(lst))
if len(lst) > 0:
    print(*lst)