def solution(lottos, win_nums):
    answer = []
    znum = 0
    wnum = 0
    for i in lottos:
        if i == 0:
            znum += 1
        for j in win_nums:
            if i == j:
                wnum += 1
    en = [6, 6, 5, 4, 3, 2, 1]
    answer.append(en[znum+wnum])
    answer.append(en[znum])
    return answer
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))