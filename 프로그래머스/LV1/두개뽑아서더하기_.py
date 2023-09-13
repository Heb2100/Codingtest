from itertools import combinations

test = [2,1,3,4,1]
perm = list(combinations(test, 2))
perm_sum = [sum(i) for i in perm]
perm_sum.sort()
perm_sum = set(perm_sum)
perm_sum = list(perm_sum)
print(perm_sum)