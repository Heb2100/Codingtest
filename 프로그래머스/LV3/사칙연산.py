
def solution(arr):
    answer = -1
    answer_list = []
    for idx, i in enumerate(arr):
        if i in ["-"]:
            print(calculate(arr[0:idx]), calculate(arr[idx+1:]))
            answer_list.append(calculate(arr[0:idx])-calculate(arr[idx+1:]))
    return max(answer_list)

def calculate(input):
    temp_sign = 0;temp_num = 0;
    for i in input:
        if temp_sign == 0 and i not in ["+", "-"]:
            temp_num = int(i)
        if i in ["+"]:
            temp_sign = 1
        if i in ["-"]:
            temp_sign = 2
        if i not in ["+", "-"]:
            if temp_sign == 1:
                temp_num += int(i); temp_sign = 0
            if temp_sign == 2:
                temp_num -= int(i); temp_sign = 0
    return temp_num


print(solution(["1", "-", "3", "+", "5", "-", "8"]))