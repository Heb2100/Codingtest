import sys
from itertools import combinations
t = int(sys.stdin.readline())
n_list = []
s_lists = []
for i in range(t):
    n = int(sys.stdin.readline())
    n_list.append(n)
    s_list = []
    for j in range(n):
        s_list.append(list(map(int, input().split()))[1:])
    s_lists.append(s_list)

def list_append(targets, s_list):
    answer = []
    if (targets == [()]): return 0
    for target in targets:
        answer += s_list[target]
        answer = list(set(answer))
    return len(list(set(answer)))

def answer(n, s_list):
    test_list = []
    answer_list = []
    for i in range(n, -1, -1):
        test_list.append(list(combinations(range(n), i)))
    max = list_append(test_list[0][0], s_list)
    for targets in test_list:
        for target in targets:
            candidate = list_append(target, s_list)
            if candidate == max -1: return candidate
            answer_list.append(candidate)
    return list(set(answer_list))[-2]

for i in range(t):
    print(answer(n_list[i], s_lists[i]))

    