# 10825
N = int(input())
grade = []
for _ in range(N):
    name, kor, eng, math = input().split()
    arr = []
    for n in name:
        arr.append(ord(n))
    grade.append([arr, int(kor), int(eng), int(math)])

grade.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for x in grade:
    name = ''
    for num in x[0]:
        name += chr(num)
    print(name)