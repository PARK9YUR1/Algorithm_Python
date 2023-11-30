N = int(input())
score = 0
grade = list(map(int, input().split()))
arr = [0]*N

for i in range(N):
    if grade[i] == 1:
        arr[i] = arr[i-1] + 1

print(sum(arr))