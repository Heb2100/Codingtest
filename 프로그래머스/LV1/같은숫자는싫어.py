def solution(arr):
    answer = list(set(arr))
    return set(arr)
# list(set(arr))는 sort() 된상태로 내보내서 안됨

def solution(arr):
    answer = []; last_i = -1
    for i in arr:
        if i != last_i:
            answer.append(i)
        last_i = i
    return answer

# 통과, -1 인 이유는 1000000 이하의 자연수라길래..

print(solution([1,1,3,3,0,1,1]))