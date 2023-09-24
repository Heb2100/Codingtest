<<<<<<< HEAD
def solution(numbers):
    from itertools import permutations
    answer = list(permutations(numbers, len(numbers)))
    ans_append = [''.join(map(str, i)) for i in answer]
    return (max(ans_append))
=======
# def solution(numbers):
#     from itertools import permutations
#     answer = list(permutations(numbers, len(numbers)))
#     ans_append = [''.join(map(str, i)) for i in answer]
#     return (max(ans_append))
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292

# 1 - 11 시간초과로 실패

def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x:x*3, reverse=True)
    return ''.join(answer)
<<<<<<< HEAD
# 11 실패

def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x:x*3, reverse=True)
    return str(int(''.join(answer)))
#  정답!
=======

>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
print(solution([6, 10, 2]))