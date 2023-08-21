# 동적 프로그래밍 & 경우의 수 알고리즘
def solution(n, money):
    # dp = [1, 0, 0, 0, 0, 0]
    dp = [1] + [0] * n

    # 1, 2, 5
    for coin in money:
        # 1 ~ 5, 2 ~ 5, 5 ~ 5
        for price in range(coin, n + 1):
            # 1, 2, 3, 4, 5
            # 2, 3, 4, 5,
            # 5
            if price >= coin:
                dp[price] += dp[price - coin]

    return dp[n] % 1000000007