def solution(nums):
    from collections import Counter
    answer = 0
    unique_nums = set(list(nums))
    if len(unique_nums) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(unique_nums)

print(solution([3, 3, 3, 2, 2, 2]))