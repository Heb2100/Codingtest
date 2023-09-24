<<<<<<< HEAD
import sys

a = int(sys.stdin.readline())
length_l = []
total_l = []
for i in range(a):
    n = int(sys.stdin.readline())
    length_l.append(n)
    l = []
    for j in range(n):
        tmp_l = []
        tmp_l = list(map(int, input().split()))
        l.append(tmp_l)
    total_l.append(l)

for i in range(a):
    l = []
    for j in range(length_l[i]):
        l.append(total_l[i][j][0] + ((total_l[i][j][1]+1)//2-1))
=======
import sys

a = int(sys.stdin.readline())
length_l = []
total_l = []
for i in range(a):
    n = int(sys.stdin.readline())
    length_l.append(n)
    l = []
    for j in range(n):
        tmp_l = []
        tmp_l = list(map(int, input().split()))
        l.append(tmp_l)
    total_l.append(l)

for i in range(a):
    l = []
    for j in range(length_l[i]):
        l.append(total_l[i][j][0] + ((total_l[i][j][1]+1)//2-1))
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
    print(min(l))