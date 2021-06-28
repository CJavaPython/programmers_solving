def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if len(scoville) <= 1:
            answer = -1
            break
        
        if scoville[0] < K:
            new_scoville = scoville[0] + (scoville[1] * 2)
            scoville.pop(0)
            scoville.pop(0)
            scoville.append(new_scoville)
            scoville.sort()
            answer += 1
        else:
            break
        
    return answer
