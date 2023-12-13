def solution(phone_book):
    answer = True
    
    phone_book.sort()
    N = len(phone_book)
    phone = phone_book[0]
    
    for i in range(1, N):
        if phone in phone_book[i]:
            length = len(phone)
            if phone_book[i][:length] == phone:
                answer = False
        phone = phone_book[i]
    
    return answer