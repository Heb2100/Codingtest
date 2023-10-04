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
    n, x, y = readInts()
    lcm = find_lcm(x, y)
    plus = n//x - n//lcm
    minus = n//y - n//lcm
    print('lcm, plus, minus', lcm, plus, minus);exit(1)
    ans = [int(((n*2-plus+1)*plus-(minus+1)*minus)/2)]
    return ans

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return x * y // find_gcd(x, y)
 
for _ in range(int(input())):
    print(*solve())