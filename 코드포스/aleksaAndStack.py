import sys
t = int(sys.stdin.readline())
n_list = []
for i in range(t):
    n_list.append(int(input()))

def answer(n):
    answer_list = []
    for i in range(n):
        answer_list.append(str(2*i + 1))
    return ' '.join(answer_list)

for i in range(t):
    print(answer(n_list[i]))