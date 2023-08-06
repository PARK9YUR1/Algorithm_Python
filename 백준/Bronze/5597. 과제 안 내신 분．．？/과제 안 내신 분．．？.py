student = []
for i in range(1, 31) :
    student.append(i)

hw_list = []
for i in range(28) :
    N = int(input())
    hw_list.append(N)

not_list = list(set(student) - set(hw_list))
print(min(not_list))
print(max(not_list))