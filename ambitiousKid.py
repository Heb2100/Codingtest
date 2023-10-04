import sys
a = int(sys.stdin.readline())
g = []
g = list(map(int, input().split()))
for i in range(len(g)):
    g[i] = abs(g[i])
print(min(g))