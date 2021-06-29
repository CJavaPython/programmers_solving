def solution(answers):
    pattern1 = '12345'
    pattern2 = '21232425'
    pattern3 = '3311224455'
    score = [0,0,0]
    result=[]
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(answers)]:
            score[0]+=1
        if answer == pattern2[idx%len(answers)]:
            score[1]+=1
        if answer == pattern3[idx%len(answers)]:
            score[2]+=1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result