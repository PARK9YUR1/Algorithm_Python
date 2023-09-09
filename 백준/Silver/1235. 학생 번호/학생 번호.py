N = int(input())
nums = []
for _ in range(N):
    num = input()
    K = k = len(num)
    nums.append(num)

lst = []
while True:
    lst = []
    k -= 1
    for number in nums:
        number = number[K-k:]
        lst.append(number)
    lst = set(lst)
    if len(lst) < N:
        k += 1
        break
print(k)