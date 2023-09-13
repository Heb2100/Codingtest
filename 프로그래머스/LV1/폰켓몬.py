def solution(nums):
    from collections import Counter
    answer = 0
    dic = Counter(nums)
    unique_nums = set(nums)
    unique_nums = list(unique_nums)
    temp_list = []
    return dic
    for num in unique_nums:
        if dic[num] >= len(nums):
            return len(nums)/2
        else:
            temp_list.append(dic[num])
    return max(temp_list)

print(solution([3, 3, 3, 2, 2, 2]))