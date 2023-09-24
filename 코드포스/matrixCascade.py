<<<<<<< HEAD
import sys
a = int(sys.stdin.readline())
input = []
g = []
for i in range(a):
    length = int(sys.stdin.readline())
    input.append(length)
    list = []
    for i in range(length):
        input = []
        input.append(sys.stdin.readline())
        list.append(input)
    g.append(list)
=======
import sys
a = int(sys.stdin.readline())
input = []
g = []
for i in range(a):
    length = int(sys.stdin.readline())
    input.append(length)
    list = []
    for i in range(length):
        input = []
        input.append(sys.stdin.readline())
        list.append(input)
    g.append(list)
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
print(a, input, g)