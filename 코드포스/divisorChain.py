import sys, math

def answer(x):    
    binary = decimal_to_binary(x)
    length = len(decimal_to_binary(x))
    step1_answer = step1(x, binary, length)
    return step2(step1_answer)

def decimal_to_binary(n):
    binary = bin(n)
    binary_str = binary[2:]  # '0b' 제거
    return binary_str

def step1(input, binary, length):
    answer = []
    answer.append(input)
    for i in range(length - 1, 0, -1):
        if int(binary[i]) == 1:
            input = input - 2**(length - i-1)
            answer.append(input)
    return answer

def step2(input):
    power_of_2 = input[-1]
    while power_of_2 > 1:
        power_of_2 = int(power_of_2/2)
        input.append(power_of_2)
    return input

a = int(sys.stdin.readline())
g = []
for _ in range(a):
    g.append(int(input()))

for i in range(a):
    ans = answer(g[i])
    length = len(ans)
    ans = ' '.join(map(str, ans))
    print(length)
    print(ans)