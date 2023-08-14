T = int(input())

for testcase in range(T):
    C = int(input()) # 단위 : 센트(0.01달러)
    quarter = C // 25
    dime = (C - quarter*25) // 10
    nickel = (C - quarter*25 - dime*10) // 5
    penny = (C - quarter*25 - dime*10 - nickel*5) // 1
    print(quarter, dime, nickel, penny)
    