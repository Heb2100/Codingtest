import sys
t = int(sys.stdin.readline())
g = []
for I in range(t):
    g.append(list(map(int, input().split())))

def res(x, y, n):
    list = []
    list.append(x)
    for a in range(n-2, -1, -1):
        list.append(y-int(a*(a+1)/2))
    ans = ' '.join(map(str, list))
    print(-1 if y-x < n*(n-1)/2 else ans)

for i in range(t):
    res(g[i][0], g[i][1], g[i][2])