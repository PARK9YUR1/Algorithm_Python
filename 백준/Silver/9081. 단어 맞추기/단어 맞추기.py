# 9081

N = int(input())
for _ in range(N):
    word = list(input())
    nums = [ord(w) for w in word]

    check = False
    for i in range(len(nums)-1, -1, -1):
        if check == True:
            break
        for j in range(len(nums)-1, i, -1):
            if check == True:
                break
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                arr = nums[i+1:]
                arr.sort()
                nums = nums[:i+1] + arr
                check = True

    new_word = ''.join([chr(n) for n in nums])
    print(new_word)