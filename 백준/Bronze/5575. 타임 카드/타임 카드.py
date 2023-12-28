for _ in range(3):
    arr = list(map(int, input().split()))
    start = arr[0]*3600+arr[1]*60+arr[2]
    end   = arr[3]*3600+arr[4]*60+arr[5]
    time = end - start
    h, time = time//3600, time%3600
    m, time = time//60,   time%60
    s       = time
    print(h, m, s)
