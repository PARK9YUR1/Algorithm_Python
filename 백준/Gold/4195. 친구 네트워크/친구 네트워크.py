import sys
input = sys.stdin.readline

# x 의 대표자(부모)
def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])  # 경로 압축
        return parents[x]

# x와 y과 속한 두개 그룹을 병합
def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parents[x] = y
        cnt[y] += cnt[x]

tc = int(input())
for _ in range(tc):
    F = int(input())  # 친구 관계의 수
    user_num = dict()
    cnt = dict()
    num = 1
    parents = [0]

    for _ in range(F):
        id1, id2 = map(str, input().rstrip().split())
        if id1 not in user_num:
            user_num[id1] = num
            cnt[num] = 1
            parents.append(num)
            num += 1
        if id2 not in user_num:
            user_num[id2] = num
            cnt[num] = 1
            parents.append(num)
            num += 1
        union(user_num[id1], user_num[id2])
        print(cnt[find(user_num[id1])])