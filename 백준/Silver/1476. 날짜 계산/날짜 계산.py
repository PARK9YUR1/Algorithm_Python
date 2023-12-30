E, S, M = map(int, input().split())
year = 1

while True:
    if (year-E) % 15 == (year-S) % 28 == (year-M) % 19 == 0:
        break
    year += 1

print(year)