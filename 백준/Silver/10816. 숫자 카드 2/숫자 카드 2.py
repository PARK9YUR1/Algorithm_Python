import sys
input = sys.stdin.readline

N = int(input())
card = {}
for num in input().split():  # 상근이 숫자 카드
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

M = int(input())
find = list(map(int, input().split()))  # 찾아야 할 카드

for cd in find:
    cd = str(cd)
    if cd in card:
        print(card[cd], end=' ')
    else:
        print(0, end=' ')