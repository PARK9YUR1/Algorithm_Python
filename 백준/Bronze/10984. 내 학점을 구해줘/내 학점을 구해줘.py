T = int(input())
for _ in range(T):
    N = int(input())
    total_C = total_G = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total_C += C
        total_G += G*C
    print(int(total_C), round(total_G/total_C, 1))