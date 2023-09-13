from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    sum1 = sum(dq1)
    sum2 = sum(dq2)
    sum_total = sum1 + sum2
    lim = len(dq1)*4
    round = 0

    if sum_total%2 != 0:
        return -1

    while True:
        if sum1 > sum2:
            val = dq1.popleft()
            dq2.append(val)
            sum1 -= val
            sum2 += val
            round += 1
        elif sum1 < sum2:
            val = dq2.popleft()
            dq1.append(val)
            sum1 += val
            sum2 -= val
            round += 1
        else:
            break
        if round == lim:
            return -1

    return round
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))