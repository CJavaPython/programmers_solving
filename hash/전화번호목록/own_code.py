#첫코드
"""def solution(phone_book):
    answer = True
    num = 0
    while num < len(phone_book):
        x = phone_book[num]
        phone_book.remove(x)
        num2 = 0
        while num2 < len(phone_book):
            if x in phone_book[num2]:
                answer = False
                break
            num2+=1
        phone_book.insert(num,x)
        num+=1
    return answer"""
#효율성 0점 정확도 : 11/13
#수정 코드
def solution(phone_book):
    answer = True
    num = 0
    phone_book.sort()
    for i in range(len(phone_book) - 1):
       if phone_book[i] in  phone_book[i+1][:len(phone_book[i])]:
           return False
    return True