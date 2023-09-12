import sys
x = int(sys.stdin.readline())
g = []
for _ in range(x):
    g.append(list(map(int, input().split())))
    g.append(str(sys.stdin.readline()))

def logic(n, a, q, log):
    print(n, a, q, log)
    maybe_flag = 0
    is_connect = a
    total_connect = a
    if is_connect == n: return 'YES'
    if total_connect == n: maybe_flag = 1
    for i in range(q):
        if log[i] == '+':
            is_connect += 1; total_connect +=1
        else:
            is_connect -= 1
        if is_connect == n: return 'YES'
        if total_connect == n: maybe_flag = 1
    if maybe_flag == 1: return 'MAYBE' 
    else: return 'NO'

ans = []
for j in range(x):
    tmp = logic(g[2*j][0], g[2*j][1], g[2*j][2], g[2*j + 1])
    ans.append(tmp)
print('\n'.join(ans))
