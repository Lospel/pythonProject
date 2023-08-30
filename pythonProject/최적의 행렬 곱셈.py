# DP 동적 프로그래밍 Top - Down 방식
def solution(matrix_sizes):
    dp = [[0 for j in range(len(matrix_sizes))] for i in range(len(matrix_sizes))]

    for gap in range(1, len(matrix_sizes)):  # gap은 곱할 두 행렬간의 간격 ex) 1 ~ 2
        for start in range(len(matrix_sizes) - gap):  # 0 ~ 2
            e = start + gap  # 0 + 1
            top_down = list()

            for m in range(start, e):  # 0 ~ 0
                top_down.append(
                    # dp[0][0] + dp[1][0] + ms[0][0] * ms[0][1] * ms[1][1]
                    dp[start][m] + dp[m + 1][e] +
                    (matrix_sizes[start][0] * matrix_sizes[m][1] * matrix_sizes[e][1]))

            dp[start][e] = min(top_down)

    return dp[0][-1]
