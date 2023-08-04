N, M = map(int, input().split())
basket = [0] * N

for num in range(M) :
    i, j, k = map(int, input().split())
    for idx in range(i, j+1) :
        basket[idx-1] = k
for num2 in range(N) :
    print(basket[num2], end=' ')