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
    n = readInt()
    c = readList()
    k = readInt()
    ans = [[0] for i in range(n)]
    minimum = min(c)
    diff = min_index = 0
    for i in range(len(c)-1, -1, -1):
        if c[i] == minimum:
            diff = k % minimum; min_index = i
            for j in range(i):
                ans[j].remove(0)
                ans[j].append(k//minimum)
    if diff != 0:
        if diff >= min(c[min_index:]):
            
    return ans
 
 
for _ in range(int(input())):
    print(*solve())