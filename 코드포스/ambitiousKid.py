<<<<<<< HEAD
import sys
a = int(sys.stdin.readline())
g = []
g = list(map(int, input().split()))
for i in range(len(g)):
    g[i] = abs(g[i])
=======
import sys
a = int(sys.stdin.readline())
g = []
g = list(map(int, input().split()))
for i in range(len(g)):
    g[i] = abs(g[i])
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
print(min(g))