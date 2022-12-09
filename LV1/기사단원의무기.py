# def solution(number, limit, power):
#     answer = 0
#     for i in range(1, number+1):
#         temp = measure(i)
#         if temp > limit:
#             answer += power
#         else:
#             answer += temp
#     return answer
    

# def measure(input):
#     answer = 0
#     for i in range(1, input+1):
#         if input % i == 0:
#             answer += 1
#     return answer

#  시간초과

import math 

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        temp = measure(i)
        if temp > limit:
            answer += power
        else:
            answer += temp
    return answer
    

def measure(input):
    answer = 0
    for i in range(1, math.ceil(math.sqrt(input+1))):
        if input % i == 0:
            answer += 2
        if input == i*i:
            answer = answer - 1
    return answer