def solution(orders, course):
    answer = []
    from collections import Counter
    from itertools import combinations
    ans_list = []
    for i in orders:
        for j in range(2, len(i)+1):
            for c in combinations(i, j):
                ans_list.append("".join(c))
    target = Counter(ans_list).most_common()
    for t in target:
        for i in course:
            temp = []
            if i == t[1]:
                temp.append(t[0])
            print(temp)

    return target
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
