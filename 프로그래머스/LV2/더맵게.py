from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    for i in range(len(scoville)):
        if len(scoville) == 1:
            if scoville[0]>=K:
                return len(scoville) -1
            else:
                return -1
        temp_1 = heappop(scoville)
        temp_2 = heappop(scoville)
        if temp_1 >= K:
            return answer
        answer += 1
        heappush(scoville, temp_1+temp_2*2)
#  이게 왜안되는거지?? 16 하나만 안된다..

from heapq import *
def solution(scoville, K):
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= K else -1
#  이거는 성공

print(solution([1, 2, 3, 9, 10, 12], 7))