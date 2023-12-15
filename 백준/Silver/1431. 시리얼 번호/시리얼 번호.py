# 1431
N = int(input())
codes = [input() for _ in range(N)]
codes.sort(key=lambda x:(len(x), sum(int(n) for n in x if n.isdigit()), x))

for code in codes:
    print(code)