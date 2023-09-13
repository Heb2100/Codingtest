import math 

def solution(n):
    answer = 0
    candid = []

    for i in measure(n):
        candid.append(i-1)
        candid.append(i+1)

    candid.sort()
    candid.unique()
    candid.remove(0)

    for i in candid:
        if n%i == 1:
            answer = i
            break
    
    return candid

def measure(input):
    answer = []
    for i in range(1, math.ceil(math.sqrt(input+1))):
        if input % i == 0:
            answer.append(i)
            answer.append(int(input/i))
        if input == i*i:
            answer.remove(i)
    answer.sort()
    return answer

print(solution(12))