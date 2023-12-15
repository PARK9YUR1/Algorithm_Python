# 16435
N, L = map(int, input().split())  # 과일개수, 초기길이
h_list = list(map(int, input().split()))
h_list.sort()

for h in h_list:
    if h <= L:
        L += 1

print(L)