<<<<<<< HEAD
def solution(N, number):
    N_list = []

    for cnt in range(1, 9):
        partial_set = set()
        partial_set.add(int( str(N) * cnt ))
        for i in range(cnt-1):
            for m in N_list[i]:
                for n in N_list[-i-1]:
                    partial_set.add(m+n)
                    partial_set.add(m-n)
                    partial_set.add(m*n)
                    if n != 0:
                        partial_set.add(m/n)
        if number in partial_set:
            return cnt
        N_list.append(partial_set)
    return -1
=======
def solution(N, number):
    N_list = []

    for cnt in range(1, 9):
        partial_set = set()
        partial_set.add(int( str(N) * cnt ))
        for i in range(cnt-1):
            for m in N_list[i]:
                for n in N_list[-i-1]:
                    partial_set.add(m+n)
                    partial_set.add(m-n)
                    partial_set.add(m*n)
                    if n != 0:
                        partial_set.add(m/n)
        if number in partial_set:
            return cnt
        N_list.append(partial_set)
    return -1
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
print(solution(5, 12))