import math
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(1, math.floor(len(score)/m)+1):
        answer += score[m*i-1]*m
    return answer