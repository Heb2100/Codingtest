def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
    for i in range(1, len(triangle)-1):
        for j in range(1, i+1):
            triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
    return max(triangle[-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))