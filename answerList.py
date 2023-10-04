import sys, math
def measure(input):
    answer = 0
    for i in range(1, math.ceil(math.sqrt(input+1))):
        if input % i == 0:
            answer += 2
        if input == i*i:
            answer = answer - 1
    return answer

def smallest_measure(input):
    answer = 0
    for i in range(2, math.ceil(math.sqrt(input+1))):
        if input % i == 0:
            return input

def answer_list(input, list):
    if list == []:
        list.append(input)
        answer_list(input, list)
    if input == 1:
        list.append(1)
        return list
    if measure(input) == 2:
        list.append(input - 1)
        answer_list(input - 1, list)
    else:
        divisor = smallest_measure(input)
        list.append(divisor)
        answer_list(input - divisor, list)

