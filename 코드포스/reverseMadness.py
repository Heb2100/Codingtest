import sys
t = int(sys.stdin.readline())
nk_list = []; str_list = []; l_lists = []; r_lists = []; q_list = []; x_lists=[]
for i in range(t):
    nk_list.append(list(map(int, input().split())))
    str_list.append(str(input()))
    l_lists.append(list(map(int, input().split()))); r_lists.append(list(map(int, input().split())))
    q_list.append(int(input())); x_lists.append(list(map(int, input().split())))

def change(k, l_list, r_list, q, x_list):
    change_list = []
    for i in range(k):
        for j in range(q):
            if (l_list[i] <= x_list[j]) and (x_list[j] <= r_list[i]):
                change_list.append([min(x_list[j], l_list[i]+r_list[i]-x_list[j]), max(x_list[j], l_list[i]+r_list[i]-x_list[j])])
    return change_list

def answer(str, change_list):
    answer = str
    for i in change_list:
        answer = answer[0:i[0]-1]+''.join(reversed(answer[i[0]-1:i[1]]))+answer[i[1]:]
    return answer

for i in range(t):
    print(answer(str_list[i], change(nk_list[i][1], l_lists[i], r_lists[i], q_list[i], x_lists[i])))