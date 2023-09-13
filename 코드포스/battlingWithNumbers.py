import sys

def answer(X, Y, X_primenum, Y_primenum, X_com, Y_com):
    if X % Y != 0: return 0
    cnt = X_primenum
    for i in range(Y_primenum):
        for j in range(X_primenum):
            if Y_com[0][i] == X_com[0][j]:
                if Y_com[1][i] == X_com[1][j]:
                    cnt -= 1
    return 2 ** cnt % 998244353

X_com = []
Y_com = []
X_primenum = int(sys.stdin.readline())
for _ in range(2):
    X_com.append(list(map(int, input().split())))
Y_primenum = int(sys.stdin.readline())
for _ in range(2):
    Y_com.append(list(map(int, input().split())))

X = 1
Y = 1
for i in range(X_primenum):
    X *= X_com[0][i] ** X_com[1][i]
for i in range(Y_primenum):
    Y *= Y_com[0][i] ** Y_com[1][i]

if X > Y: ans = answer(X, Y, X_primenum, Y_primenum, X_com, Y_com) 
elif X == Y: ans = 1
else: ans = answer(Y, X, Y_primenum, X_primenum, Y_com, X_com)

print(ans)

