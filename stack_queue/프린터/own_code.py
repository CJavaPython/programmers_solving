def solution(priorities, location):
    answer = 1
    count = 0
    q = []
    l = len(priorities)
    while count < l:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            if count == location:
                return answer
            answer += 1
        else:
            q.append([priorities[0], count])
            priorities.pop(0)
        count += 1
    count = 0
    while len(q) > 0:
        if q[0][0] == max(q[0:][0]):
            count = q[0][1]
            q.pop(0)
            if count == location:
                return answer 
            answer += 1
        else:
            tmp = q[0]
            q.pop(0)
            q.append(tmp)
    return answer
#result : 8/20