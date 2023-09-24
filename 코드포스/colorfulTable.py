import sys
a = int(sys.stdin.readline())

nt_lists = []
a_lists = []
for i in range(a):
    nt_lists.append(list(map(int, input().split())))
    a_lists.append(list(map(int, input().split())))

def answer(nt_list, a_list):
    answer_list = []
    unique_a_list = list(set(a_list))
    for i in range(nt_list[1]):
        if i+1 in unique_a_list: answer_list.append(square_finder(nt_list[0], a_list, i+1)) 
        else: answer_list.append(str(0))
    return ' '.join(answer_list)

def square_finder(n, a_list, target):
    square_length = n
    for i in range(n):
        if a_list[i] >= target : break
        else : square_length -= 1
    for i in range(n-1, -1, -1):
        if a_list[i] >= target : break
        else : square_length -= 1
    return str(square_length * 2)

for i in range(a):
    print(answer(nt_lists[i], a_lists[i]))

