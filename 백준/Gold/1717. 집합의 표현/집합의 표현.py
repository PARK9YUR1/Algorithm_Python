import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# x 의 대표자(부모)
def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])  # 경로 압축
        return parents[x]


# x와 y과 속한 두개 그룹을 병합
def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parents[px] = py

n, m = map(int, input().split())  # m : 입력으로 주어지는 연산의 개수
parents = [i for i in range(n+1)]
for _ in range(m):
    # c = 0 -> 합집합 : a 포함된 집합과 b 포함된 집합 합침
    # c = 1 -> 확인 : a와 b가 같은 집합에 포함되어 있는지 확인
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        A, B = find(a), find(b)
        if A == B:
            print('YES')
        else:
            print('NO')