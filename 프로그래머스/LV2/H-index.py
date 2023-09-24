def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    last_paper_num = 0; last_i = 0;
    for idx, i in enumerate(citations):
        paper_num = idx+1
        if paper_num > i:
            return min(last_paper_num, last_i)
        last_paper_num = paper_num
        last_i = i
<<<<<<< HEAD
# 9 실패, 아마 7, 6, 5 이런걸 생각을 안한듯
print(solution([3, 0, 6, 1, 5]	))
def solution(citations):
    answer = 0
    citations.sort(reversed)
    last_paper_num = 0; last_i = 0;
    for idx, i in enumerate(citations):
        paper_num = idx+1
        if paper_num > i:
            return min(last_paper_num, last_i)
        last_paper_num = paper_num
        last_i = i
    return last_paper_num
# 통과!
=======
    return citations
print(solution([3, 0, 6, 1, 5]	))
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
