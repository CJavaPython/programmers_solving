def solution(progresses,speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] = progresses[i] + speeds[i]
            count += 1
        tmp.append(count)
    bar = 0
    for j in range(len(tmp)):
        if j == 0:
            continue
        if tmp[j] > max(tmp[bar:j]):
            answer.append(j - bar)
            bar = j
        else:
            pass



    return answer
