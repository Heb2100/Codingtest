from heapq import heappop, heappush, heappushpop

numbers = []

numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)


x = numbers.popleft()
print(x)
y = numbers.popleft()
print(y)
print(numbers)
print(len(numbers))
# 실행결과
# 3
# 4
# deque([5, 6])
# 2