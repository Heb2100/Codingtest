def solution(participant, completion):
    dic = {}
    temp = 0
    for runner in participant:
        dic[hash(runner)] = runner
        temp += hash(runner)
    for runner in completion:
        temp -= hash(runner)
    return dic
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))