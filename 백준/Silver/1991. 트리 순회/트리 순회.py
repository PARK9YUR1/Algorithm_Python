def func(p, N, k):
    if p < 0:
        return

    if p < N:
        # 전위
        if k == 1:
            print(chr(p+65), end='')
            func(tree[p][0], N, k)
            func(tree[p][1], N, k)
        # 중위
        if k == 2:
            func(tree[p][0], N, k)
            print(chr(p+65), end='')
            func(tree[p][1], N, k)
        # 후위
        if k == 3:
            func(tree[p][0], N, k)
            func(tree[p][1], N, k)
            print(chr(p+65), end='')

N = int(input())
tree = [[-1, -1] for _ in range(N)]
for _ in range(N):
    P, C1, C2 = map(str, input().split())
    i = ord(P)-65
    if C1 != '.':
        tree[i][0] = ord(C1)-65
    if C2 != '.':
        tree[i][1] = ord(C2)-65

func(0, N, 1)
print()
func(0, N, 2)
print()
func(0, N, 3)
