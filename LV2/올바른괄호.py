# def solution(s):
#     left = 0 ; right = 0
#     for i in range(len(s)):
#         if s[0] == ')' or s[len(s)-1] == '(':
#             return False
#         #  첫번째, 마지막 괜찮나?
#         if s[i] == '(':
#             left += 1
#         else:
#             right += 1
#         #  개수가 맞는가?
#     if left == right:
#         return True
#     else:
#         return False
# 5, 11 실패!


def solution(s):
    left = 0 ; right = 0; overload = 0
    if s[0] == ')' or s[len(s)-1] == '(':
            return False
        #  첫번째, 마지막 괜찮나?
    for i in range(len(s)):
        
        if s[i] == '(':
            left += 1
            overload += 1
        else:
            right += 1
            overload -= 1
        #  개수가 맞는가?
        if overload < 0:
            return False
        #  '())))' 가 생겼는가?

    if left == right:
        return True
    else:
        return False

print(solution("(())()"))