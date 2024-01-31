N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

while K > 0:
    arr = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    K -= 1

arr = [str(arr[i]) for i in range(len(arr))]
print(','.join(arr))