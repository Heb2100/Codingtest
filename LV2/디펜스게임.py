# def solution(n, k, enemy):
#     answer = 0
#     candid = []
#     for i in enemy:
#         candid.append(i)
#         test = candid
#         test.sort()
#         test = test[:-k]
#         if n < sum(test):
#             break
#         answer += 1
#     return answer
# 3,6,7,8,9,10 시간초과... 아이디어가 안떠오른다... heap을 쓰면 될까?
# 빈 list 를 sum 하면 0이 나온다는걸 알게됨


def solution(n, k, enemy):
    from heapq import heappushpop, heappush
    heap = []
    sum_total = round = 0
    for i in enemy:
        sum_total += i
        if sum_total <= n:
            heappush(heap, -i)
            round += 1
        else:
            if k>0:
                k-= 1
                sum_total += heappushpop(heap, -i)
                round += 1
    return round
print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
    
