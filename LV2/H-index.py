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
    return citations
print(solution([3, 0, 6, 1, 5]	))