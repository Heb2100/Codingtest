from collections import Counter
def solution(k, tangerine):
    answer = 0; sum = 0
    tan = Counter(tangerine).most_common()
    print(tan)
    for t in tan:
        print(t)
        sum += t[1]
        answer += 1
        if sum >= k:
            break
    return answer
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))