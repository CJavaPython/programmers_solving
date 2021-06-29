def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key=lambda number: (number[0], number[1%len(number)], number[2%len(number)], number[3%len(number)]) , reverse=True)
    for j in range(len(numbers)):
        answer = answer + numbers[j]
    if answer == '' or int(answer) == 0:
        answer = '0'
    return answer