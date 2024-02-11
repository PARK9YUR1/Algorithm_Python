arr = [int(input()) for _ in range(9)]
arr.sort()

x = sum(arr) - 100

def func():
    for i in range(9):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == x:
                return arr[:i] + arr[i+1:j] + arr[j+1:]
    
result = func()

for res in result:
    print(res)