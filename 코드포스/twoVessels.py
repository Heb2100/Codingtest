import sys
a = int(sys.stdin.readline())
g = []
for i in range(a):
    l = []
    l = list(map(int, input().split()))
    g.append(l)
for i in range(a):
    rest = abs(g[i][0]-g[i][1]) % (2*g[i][2])
    div = abs(g[i][0]-g[i][1])//(2*g[i][2])
    print(div if rest == 0 else div + 1)