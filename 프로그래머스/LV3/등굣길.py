<<<<<<< HEAD

def solution(m, n, puddles):
    answer_list = [[0 for i in range(m+1)] for i in range(n+1)]
    answer_list[1][1] = 1
    for j in range(m+1):
        for i in range(n+1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles:#  얘를 안갈아줘서 계속 말썽...
                answer_list[i][j] = 0
            else:
                answer_list[i][j] = (answer_list[i-1][j] + answer_list[i][j-1])
    return answer_list[n][m]%1000000007


def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp
print(solution(4,3,[[2, 2]]))
=======

def solution(m, n, puddles):
    answer_list = [[0 for i in range(m+1)] for i in range(n+1)]
    answer_list[1][1] = 1
    for j in range(m+1):
        for i in range(n+1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles:#  얘를 안갈아줘서 계속 말썽...
                answer_list[i][j] = 0
            else:
                answer_list[i][j] = (answer_list[i-1][j] + answer_list[i][j-1])
    return answer_list[n][m]%1000000007


def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp
print(solution(4,3,[[2, 2]]))
>>>>>>> abcbe5050c8b8733e5d32056d4e0865a2a6f6292
