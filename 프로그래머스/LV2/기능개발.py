def solution(progresses, speeds):
    import math
    from collections import Counter
<<<<<<< HEAD
    work_days = []; max_day = 0
    for i in range(len(progresses)):
        work_days.append(math.ceil((100-progresses[i])/speeds[i]))
    # 일해야하는 날수 계산

=======
    work_days = []; temp_list = [1000]; cycle = 0; answer = []; max_day = 0
    for i in range(len(progresses)):
        work_days.append(math.ceil((100-progresses[i])/speeds[i]))
    # 일해야하는 날수 계산
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
    for idx, i in enumerate(work_days):
        if max_day < i:
            max_day = i
        else:
            work_days[idx] = max_day
<<<<<<< HEAD
    # [7, 3, 9] -> [7, 7, 9]

=======
    
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
    return list(Counter(work_days).values())
        

print(solution([93, 30, 55],[1, 30, 5]))