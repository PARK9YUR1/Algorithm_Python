A, B, C = map(int, input().split())
prize_money = 0

if A == B and B == C :
    prize_money = 10000 + A*1000
elif A == B and B!= C :
    prize_money = 1000 + A*100
elif B == C and C!= A :
    prize_money = 1000 + B*100
elif C == A and A!= B :
    prize_money = 1000 + C*100
else : 
    if A > B and A > C : 
        prize_money = A*100
    elif B > C and B > A : 
        prize_money = B*100
    elif C > A and C > B : 
        prize_money = C*100

print(prize_money)
        