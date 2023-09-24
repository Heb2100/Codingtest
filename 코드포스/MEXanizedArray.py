import sys
a = int(sys.stdin.readline())
g = []
for i in range(a):
    g.append(list(map(int, input().split())))
def answer(n, k, x):
    if k >= x+2 or k>=n+1 : return -1
    if x == k : x -= 1
    return int(k*(k-1)/2 + x*(n-k))

for i in range(a):
    print(answer(g[i][0], g[i][1], g[i][2]))
    