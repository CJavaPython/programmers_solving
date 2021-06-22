def solution(clothes):
    answer = {}
    for i in range(len(clothes)):
        answer[clothes[i][1]] = clothes[i][0]
        
    return answer