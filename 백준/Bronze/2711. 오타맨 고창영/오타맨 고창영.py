T = int(input())
for _ in range(T):
    idx, txt = input().split()
    idx = int(idx) - 1
    result = txt[:idx] + txt[idx+1:]
    print(result)