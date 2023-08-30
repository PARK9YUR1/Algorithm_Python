import sys
input = sys.stdin.readline

N = int(input())
lst = set()
for _ in range(N):
    name, c = map(str, input().split())
    if c == 'enter':
        lst.add(name)
    else:
        lst.remove(name)

lst = list(lst)
lst.sort(reverse=True)
for nm in lst:
    print(nm)