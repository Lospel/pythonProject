from itertools import product
def solution(n):
    left = ['(', ')']
    answer = 0

    for x in product(left, repeat=n * 2):
        if check(x):
            answer += 1

    return answer


def check(string):
    stack = []

    for bracket in string:
        if bracket == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False

    if stack:
        return False

    return True

# 카탈란 수 https://magentino.tistory.com/90
def solution2(n):
    dp = [0 for x in range(n + 1)]

    # 곱셉 규칙상 0인 괄호쌍 값은 1로 설정
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):  # 2 ~ n
        for j in range(i):  # 0 ~ 1 ... n-1
            # dp[2] += dp[0] * dp[1]
            # dp[2] += dp[1] * dp[0]
            # dp[3] += dp[0] * dp[2]
            # dp[3] += dp[1] * dp[1]
            # dp[3] += dp[2] * dp[0]
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[n]