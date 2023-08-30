import sys
input = sys.stdin.readline

N = int(input())  # 상근이 카드 개수
card = set(map(int, input().split()))  # 상근이 카드
M = int(input())  # 찾을 카드 개수
find = list(map(int, input().split()))  # 찾을 카드

for cd in find:
    if cd in card:
        print(1, end=' ')
    else:
        print(0, end=' ')