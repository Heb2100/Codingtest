def solution(nums):
    from collections import Counter
    answer = 0
<<<<<<< HEAD
    unique_nums = set(list(nums))
    if len(unique_nums) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(unique_nums)
=======
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
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292

print(solution([3, 3, 3, 2, 2, 2]))