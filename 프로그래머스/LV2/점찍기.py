
# def solution(k, d):
#     import math
#     answer = 0
#     for i in range(0, d+1, k):
#         for j in range(0, d+1, k):
#             if math.sqrt(i**2+j**2)<=d:
#                 answer += 1
#     return answer
# 실패, 시간초과

import math
d = 4; k = 2 ; answer = 0
for x in range(0, d + 1, k):
    res_d = math.floor(math.sqrt(d*d - x*x))
    # print(res_d)
    answer += (res_d // k) + 1
    print(answer)

