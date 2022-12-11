from itertools import combinations
perms = []
x = 'god'
for i in range(1, len(x)+1):
    for c in combinations(x, i):
        perms.append("".join(c))

print(perms)