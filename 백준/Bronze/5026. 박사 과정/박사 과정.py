N = int(input())
for _ in range(N):
    q = input()
    if q == "P=NP":
        print("skipped")
    else:
        nums = q.split('+')
        print(int(nums[0])+int(nums[1]))