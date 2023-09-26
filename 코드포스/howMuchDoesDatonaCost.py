import sys
t = int(sys.stdin.readline())
nk_list = []
a_lists = []
for i in range(t):
    nk_list.append(list(map(int, input().split())))
    a_lists.append(list(map(int, input().split())))

for i in range(t):
    if nk_list[i][1] in a_lists[i]: print("YES")
    else: print("NO")