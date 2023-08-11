import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

def solution(n, lighthouse):
    # 트리
    conn = defaultdict(list)

    # 양방향 트리
    for a, b in lighthouse:
        conn[a - 1].append(b - 1)
        conn[b - 1].append(a - 1)

    # 동적 프로그래밍
    visited = [False for _ in range(len(conn))]

    # 등대 값
    dp = [[0, 0] for _ in range(len(conn))]

    def dfs(node):
        visited[node] = True
        leaf_list = list()

        for leaf in conn[node]:
            if visited[leaf]:
                continue
            leaf_list.append(leaf)
            dfs(leaf)

        # 등대 불, 0 = 끄는것, 1 = 키는것
        dp[node][0] = 0
        dp[node][1] = 1

        for leaf in leaf_list:
            # 루트 노드 등대 켜기 : 자식 노드는 켜도 안켜도 상관 없으니 최소값을 더한다. 즉, 자식 노드는 최소한으로 꺼진 것으로 판단.
            dp[node][1] += min(dp[leaf])
            # 루트 노드 등대 끄기 : 자식 노드는 무조건 켜져 있어야 하니 자식 노드의 등대 값을 더한다.
            dp[node][0] += dp[leaf][1]

        return

    dfs(0)

    return min(dp[0])  # 루트 노드가 켜진 값과 꺼진 값 중의 최소값이 최소 등대 불 값이다.