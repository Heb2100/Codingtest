def solution(cloths):
    from collections import Counter
    from functools import reduce
    dic = Counter(type for name, type in cloths)
    return reduce(lambda x, y : x * (y+1), dic.values(), 1) - 1
print(solution([["yellow_hat", "headgear"], 
["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))