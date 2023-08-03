X = int(input()) # 영수증 총 금액
N = int(input()) # 구매한 물건의 종류의 수
sum = 0

for i in range(1, N+1) :
    # a:가격, b:개수
    a, b = map(int, input().split())
    sum += a * b

if sum == X : 
    print('Yes')
else : 
    print('No')