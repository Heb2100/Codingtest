def solution(s):
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx,num in enumerate(en):
        if num in s:
            s = s.replace(num, str(idx))
        answer = s
    return int(answer)

# if .. in .. 을 배움
# replace 함수를 배움