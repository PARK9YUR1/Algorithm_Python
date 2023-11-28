import sys
input = sys.stdin.readline

nums = input().rstrip()

before = 0
result = 1

for num in nums:
    if num == 'c':
        if num == before:
            result *= 25
            result %= 1000000009
        else:
            result *= 26
            result %= 1000000009
        before = num
    else:
        if num == before:
            result *= 9
            result %= 1000000009
        else:
            result *= 10
            result %= 1000000009
        before = num

print(result)