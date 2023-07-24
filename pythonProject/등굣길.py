def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(m):
            if ([x + 1, y + 1] in puddles) or ((y, x) == (0, 0)) : continue
            dp[y][x] = (dp[y-1][x] + dp[y][x - 1]) % 1000000007

    return dp[-1][-1]

def solution2(m, n, puddles):
    return dfs2(0,0,n,m,puddles)

def dfs2(y, x, row, col, puddles):
    path = [[1, 0], [0, 1]]
    answer = 0

    if [y, x] == [row - 1, col - 1]: return 1

    for i in range(2):
        ny = y + path[i][0]
        nx = x + path[i][1]

        if 0 <= ny < row and 0 <= nx < col :
            if [nx + 1, ny + 1] in puddles: continue
            answer += dfs2(ny, nx, row, col, puddles)

    return answer % 1000000007

def solution3(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    return dfs3(0,0,dp,puddles)

def dfs3(y, x, dp, puddles):
    row, col = len(dp), len(dp[0])
    path = [[1, 0], [0, 1]]

    if [y, x] == [row - 1, col - 1]: return 1
    if dp[y][x] != 0 : return dp[y][x]

    for i in range(2):
        ny = y + path[i][0]
        nx = x + path[i][1]

        if 0 <= ny < row and 0 <= nx < col :
            if [nx + 1, ny + 1] in puddles: continue
            dp[y][x] += dfs3(ny, nx, dp, puddles)

    return dp[y][x] % 1000000007