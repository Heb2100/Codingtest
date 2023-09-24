<<<<<<< HEAD
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
=======
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
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
    print(div if rest == 0 else div + 1)