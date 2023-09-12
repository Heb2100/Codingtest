def solution(sentence):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = [i for i in alphabet_list]
    from collections import Counter
    dic = list(Counter(sentence).keys())
    ans_list = []
    for i in dic:
        ans_list.append(i.lower())
    for i in ans_list:
        for j in alphabet_list:
            if i == j:
                answer.remove(i)
    if answer == []:
        return "perfect"
    return ''.join(answer)
print(solution(
"Jackdaws love my big sphinx of quartz"))