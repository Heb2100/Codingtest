<<<<<<< HEAD
t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    n, a, q = map(int, input().split())  # 구독자 수, 초기 온라인 구독자 수, 알림 개수
    notifications = input()  # 알림 정보

    online_subscribers = a  # 초기 온라인 구독자 수를 저장하는 변수
    min_online_subscribers = a  # 온라인 구독자 수의 최솟값을 저장하는 변수
    max_online_subscribers = a  # 온라인 구독자 수의 최댓값을 저장하는 변수

    for notification in notifications:
        if notification == '+':
            online_subscribers += 1
        else:
            online_subscribers -= 1

        min_online_subscribers = min(min_online_subscribers, online_subscribers)
        max_online_subscribers = max(max_online_subscribers, online_subscribers)

    if max_online_subscribers >= n and min_online_subscribers <= n:
        print("YES")
    elif min_online_subscribers > n or max_online_subscribers < 0:
        print("NO")
    else:
=======
t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    n, a, q = map(int, input().split())  # 구독자 수, 초기 온라인 구독자 수, 알림 개수
    notifications = input()  # 알림 정보

    online_subscribers = a  # 초기 온라인 구독자 수를 저장하는 변수
    min_online_subscribers = a  # 온라인 구독자 수의 최솟값을 저장하는 변수
    max_online_subscribers = a  # 온라인 구독자 수의 최댓값을 저장하는 변수

    for notification in notifications:
        if notification == '+':
            online_subscribers += 1
        else:
            online_subscribers -= 1

        min_online_subscribers = min(min_online_subscribers, online_subscribers)
        max_online_subscribers = max(max_online_subscribers, online_subscribers)

    if max_online_subscribers >= n and min_online_subscribers <= n:
        print("YES")
    elif min_online_subscribers > n or max_online_subscribers < 0:
        print("NO")
    else:
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
        print("MAYBE")