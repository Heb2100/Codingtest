def solution(new_id):
    test1 = new_id
    test1 = test1.lower()
    test = ''
    for word in test1:
        if word.isalnum() or word in '-_.':
            test += word
    test = test.replace('...', '.')
    test = test.replace('..', '.')
    if test[0] == '.' and len(test)>1:
        test = test[1:]
    if test[-1] == '.':
        test = test[:-1]
    if not test:
        test = 'a'
    test = test[:15]
    if len(test) == 1:
        test = test+test+test
    if len(test) == 2:
        test = test+test[1]
    answer = test
    return answer
print(solution("abcdefghijklmn.p"))