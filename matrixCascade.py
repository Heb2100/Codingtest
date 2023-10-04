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
print(a, input, g)