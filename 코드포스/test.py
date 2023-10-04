import sys
input = sys.stdin.readline
 
def readList():
    return list(map(int, input().split()))
def readInt():
    return int(input())
def readInts():
    return map(int, input().split())
def readStr():
    return input().strip()
 
# BF, EC, DB, CC, CL
def solve():
    n, k = readInts()
    arr = readList()
    ans = [0] * k
    idx = [[] for _ in range(k+1)]
    for i in range(n):
        idx[arr[i]].append(i+1)
    print(idx[2][-1]);exit(1)
    ma, mi = 0, n+1
    for i in range(k, 0, -1):
        if idx[i]:
            L, R = n+1, 0
            ma, mi = max(ma, idx[i][-1]), min(mi, idx[i][0])
            for j in idx[i]:
                L = min(L, min(j, mi))
                R = max(R, max(j, ma))
            ans[i-1] = (R - L + 1) * 2
    return ans
 
 
for _ in range(int(input())):
    print(*solve())