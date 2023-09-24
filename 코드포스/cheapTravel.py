<<<<<<< HEAD
g = []
g = list(map(int, input().split()))
n = g[0]
m = g[1]
a = g[2]
b = g[3]
# print((a*n-(n//m)*m*(a-b/m)) if a>b else a*n)
# print((a*n-(n//m)*(a*m-b)) if a*m>b else a*n)
=======
g = []
g = list(map(int, input().split()))
n = g[0]
m = g[1]
a = g[2]
b = g[3]
# print((a*n-(n//m)*m*(a-b/m)) if a>b else a*n)
# print((a*n-(n//m)*(a*m-b)) if a*m>b else a*n)
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
print(b*(n//m) + min(b, (n%m)*a) if a*m>b else a*n)