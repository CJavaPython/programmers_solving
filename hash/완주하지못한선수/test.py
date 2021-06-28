def solution(v):
    answer = []
    x = {}
    y = {}

    for i in range(len(v)):
        x[v[i][0]] = x.get(v[i][0], 0) + 1
        y[v[i][1]] = y.get(v[i][1], 0) + 1

    for i in x:
        if x[i] < 2:
            answer.append(i)
    for j in y:
        if y[j] < 2:
            answer.append(j)

    return answer