<<<<<<< HEAD
import heapq

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    n, m, k = map(int, input().split())  # 퀘스트 개수, 의존성 개수, 하루의 시간 단위
    h = list(map(int, input().split()))  # 각 퀘스트의 완료 시간
    dependencies = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        dependencies[b].append(a)

    in_degree = [0] * (n + 1)  # 각 퀘스트의 선행 퀘스트 개수
    for quest in dependencies:
        for pre_quest in quest:
            in_degree[pre_quest] += 1

    available_quests = []  # 선행 퀘스트가 없는 퀘스트들
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            available_quests.append(i)

    heapq.heapify(available_quests)
    completion_times = [0] * (n + 1)

    while available_quests:
        current_quest = heapq.heappop(available_quests)
        completion_times[current_quest] = h[current_quest - 1]

        for next_quest in dependencies[current_quest]:
            in_degree[next_quest] -= 1
            if in_degree[next_quest] == 0:
                heapq.heappush(available_quests, next_quest)
                h[next_quest - 1] = max(h[next_quest - 1], h[current_quest - 1])

    min_completion_time = max(completion_times)
=======
import heapq

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    n, m, k = map(int, input().split())  # 퀘스트 개수, 의존성 개수, 하루의 시간 단위
    h = list(map(int, input().split()))  # 각 퀘스트의 완료 시간
    dependencies = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        dependencies[b].append(a)

    in_degree = [0] * (n + 1)  # 각 퀘스트의 선행 퀘스트 개수
    for quest in dependencies:
        for pre_quest in quest:
            in_degree[pre_quest] += 1

    available_quests = []  # 선행 퀘스트가 없는 퀘스트들
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            available_quests.append(i)

    heapq.heapify(available_quests)
    completion_times = [0] * (n + 1)

    while available_quests:
        current_quest = heapq.heappop(available_quests)
        completion_times[current_quest] = h[current_quest - 1]

        for next_quest in dependencies[current_quest]:
            in_degree[next_quest] -= 1
            if in_degree[next_quest] == 0:
                heapq.heappush(available_quests, next_quest)
                h[next_quest - 1] = max(h[next_quest - 1], h[current_quest - 1])

    min_completion_time = max(completion_times)
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
    print(min_completion_time)