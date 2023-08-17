N = int(input())  # 숫자 개수
nums_ = list(map(int, input().split()))  # 수식에 사용되는 숫자
oper1 = list(map(int, input().split()))  # + - * / 개수 -> ex) 2 0 1 0
oper2 = {0: '+', 1: '-', 2: '*', 3: '/'}

operator = []  # ['*/++-', '/+*-+', '+*+/-', ... , '-/*++', '-*+/+']
arr = []  # ['+', '+', '-', '*', '/']
for i in range(4):
    for _ in range(oper1[i]):
        arr.append(oper2[i])

# 연산자 순열
def perm(i, N):  # i: 재귀 깊이 / N: 순열 만들 리스트 크기
    if i == N:
        operator.append(''.join(arr))
        return
    for j in range(i, N):
        arr[i], arr[j] = arr[j], arr[i]
        perm(i + 1, N)
        arr[i], arr[j] = arr[j], arr[i]

perm(0, len(arr))
operator = list(set(operator))  # ['*/++-', '/+*-+', '+*+/-', ... , '-/*++', '-*+/+']

mx = -1000000000
mn = 1000000000

def calc(operator, nums_):
    global mx, mn
    for oper in operator:  # oper : '*/++-'        operator : ['*/++-', ... , '-*+/+']
        nums = []
        for n in range(N):
            nums.append(nums_[n])

        for o in oper:     # o : *                 oper : '*/++-'
            x = nums.pop(0)
            y = nums.pop(0)
            if o == '+':
                z = x + y
            elif o == '-':
                z = x - y
            elif o == '*':
                z = x * y
            elif o == '/':
                z = int(x / y)
            nums.insert(0, z)
        if len(nums) == 1:
            result = nums[0]
        if mx < result:
            mx = result
        if mn > result:
            mn = result

calc(operator, nums_)
print(mx)
print(mn)