nums = input()

before = 0
A = 1
B = 1000000009

for num in nums:
    if num == 'c':
        if num == before:
            A *= 25
            A %= 1000000009
        else:
            A *= 26
            A %= 1000000009
        before = num
    else:
        if num == before:
            A *= 9
            A %= 1000000009
        else:
            A *= 10
            A %= 1000000009
        before = num

print(A%B)