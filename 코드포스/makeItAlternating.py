import sys, math
t = int(sys.stdin.readline())
s_list = []
for i in range(t):
    s_list.append(str(input()))

def answer(s):
    ex_char = s[0]
    answer_list = []
    tmp_add = 0; first_ans = 0; second_ans = 1
    for i in range(1, len(s)):
        if ex_char == s[i]: tmp_add += 1
        else : ex_char = s[i]; answer_list.append(tmp_add); tmp_add = 0; 
        if (i == len(s)-1): answer_list.append(tmp_add)
    for i in range(len(answer_list)):
        first_ans += answer_list[i]
        second_ans *= math.factorial(answer_list[i] + 1)
    print(first_ans, second_ans % 998244353)

for i in range(t):
    answer(s_list[i])