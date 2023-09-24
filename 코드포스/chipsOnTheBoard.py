import sys
t = int(sys.stdin.readline())

n_list = []
a_lists = []
b_lists = []
for i in range(t):
    n = int(sys.stdin.readline()); n_list.append(n)
    a_list = []; b_list = []
    a_lists.append(list(map(int, input().split()))); b_lists.append(list(map(int, input().split())))

def answer(n, a_list, b_list):
    return min(sum(a_list) + min(b_list)*n , sum(b_list) + min(a_list)*n)

for i in range(t):
    print(answer(n_list[i], a_lists[i], b_lists[i]))