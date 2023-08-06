# N: 바구니 개수, M: 바꾸는 횟수
N, M = map(int, input().split())
basket = []
for num in range(N) : 
    basket.append(num+1)

for num2 in range(M) :
    # i번 바구니, j번 바구니 교환
    i, j  = map(int, input().split())
    tmp = 0
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp

for num3 in range(N) :
    print(basket[num3], end=' ')