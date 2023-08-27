import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
P = [0] * (N+1)
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def f(x):
    for i in range(len(tree[x])):
        j = tree[x][i]
        if visited[j] == False:
            visited[j] = True
            P[j] = x
            f(j)

f(1)
for i in range(2, N+1):
    print(P[i])