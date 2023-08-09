T = int(input()) # test case

for testcase in range(T):
    r, S = map(str, input().split())
    R = int(r)
    for s in S:
        print(s*R, end='')
    print()