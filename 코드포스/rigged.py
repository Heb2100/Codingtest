import sys
t = int(sys.stdin.readline())

se_lists = []
n_list = []
for i in range(t):
    n = int(sys.stdin.readline()); n_list.append(n)
    se_list = []
    for j in range(n):
        se_list.append(list(map(int, input().split())))
    se_lists.append(se_list)

def answer(n, se_list):
    answer = se_list[0][0]
    for i in range(1, n):
        if se_list[i][0] >= answer:
            if se_list[i][1] >= se_list[0][1]:
                return -1
    return answer

for i in range(t):
    print(answer(n_list[i], se_lists[i]))
