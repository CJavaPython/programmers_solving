def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    k = sorted(numbers, key=lambda number: (number[0], number[1%len(number), number[2%len(number)], number[3%len(number)]]))
    for j in range(len(k)):
        answer = answer + k[j]
        
    return answer