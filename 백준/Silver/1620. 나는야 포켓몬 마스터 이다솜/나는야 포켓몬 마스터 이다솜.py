import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    x = input().rstrip()
    pokemon[i] = x
    pokemon[x] = i
for m in range(M):
    test = input().rstrip()
    if test.isdigit():
        print(pokemon[int(test)])
    else:
        print(pokemon[test])