def solution(n, k, enemy):
    from heapq import heappush, heappushpop
    total = 0; cycle = 0
    heap = []
    for i in enemy:
        total += i
        if n > total:
            cycle += 1
            heappush(heap, -i)
        else:
            if k>0:
                total += heappushpop(heap, -i)
                k -= 1
                cycle += 1
    return cycle
print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))