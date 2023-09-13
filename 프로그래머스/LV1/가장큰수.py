# def solution(numbers):
#     from itertools import permutations
#     answer = list(permutations(numbers, len(numbers)))
#     ans_append = [''.join(map(str, i)) for i in answer]
#     return (max(ans_append))

# 1 - 11 시간초과로 실패

def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x:x*3, reverse=True)
    return ''.join(answer)

print(solution([6, 10, 2]))