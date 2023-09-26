import sys
t = int(sys.stdin.readline())
nkx_list = []
for i in range(t):
    nkx_list.append(list(map(int, input().split())))

for i in range(t):
    print("YES" if (nkx_list[i][1]*(nkx_list[i][1]+1)/2 <= nkx_list[i][2]) and (nkx_list[i][2] <= nkx_list[i][1]*(2*nkx_list[i][0]-nkx_list[i][1]+1)/2) else "NO")