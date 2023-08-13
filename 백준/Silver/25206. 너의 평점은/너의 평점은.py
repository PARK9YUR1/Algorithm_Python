HxD = 0  # 학점 * 등급
total_H = 0 # 학점의 총합

D1 = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
D2 = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0, 0]

for _ in range(20):
    subject, H_, D_ = map(str, input().split())  # 과목명, 학점, 등급

    H = float(H_)

    for i in range(10):
        if D_ == D1[i]:
            D = D2[i]
    HxD += H * D

    if D_ != 'P':
        total_H += H

print(HxD/total_H)