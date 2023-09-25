import sys 
t = int(sys.stdin.readline())
n_list = []
a_lists = []
for i in range(t):
    n_list.append(int(input()))
    a_lists.append(list(map(int, input().split())))

b_lists = []
def answer(n, a_list):
    b_list = []
    ex_b = 0
    for i in range(n):
        next_b = ex_b+1 if (ex_b+1 != a_list[i]) else ex_b+2
        b_list.append(next_b)
        ex_b = next_b
    return b_list[n-1]

for i in range(t):
    print(answer(n_list[i], a_lists[i]))