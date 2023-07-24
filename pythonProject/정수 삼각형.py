def solution(triangle):
    height = len(triangle) - 1
    while height > 0:
        for i in range(height):
            triangle[height - 1][i] += max(triangle[height][i], triangle[height][i + 1])
        height -= 1
    return triangle[0][0]

def solution2(triangle):
    dp = [[0, *t, 0] for t in triangle]
    for i in range(1, len(triangle)):
        for j in range(1, i + 2):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])