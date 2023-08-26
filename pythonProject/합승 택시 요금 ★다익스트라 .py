import heapq
def solution(n, s, a, b, fares):
    answer = 10000000
    graph = [[] for _ in range(n + 1)]  # 1번 노드부터 시작하므로 하나더 추가
    for x in fares:
        node1, node2, fee = x
        # 정방향
        graph[node1].append((node2, fee))
        # 역방향
        graph[node2].append((node1, fee))

    distance_list = [[]] + [dijkstra(n, i, graph) for i in range(1, n + 1)] # 0번은 빈칸 + 1번부터 n번까지 노드부터 리프까지의 거리값

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)

    return answer


def dijkstra(n, s, graph):
    q = []
    # 최단거리 초기화
    distance = [10000000] * (n + 1)
    # 시작노드 설정
    heapq.heappush(q, (0, s))
    # 시작노드 비용
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 계산된 거리값은 스킵
        if distance[now] < dist:
            continue
        # graph[1]..[n] / graph[1] = [(4, 10), (3, 41), (5, 24), (6, 25)]
        # 다익스트라 알고리즘의 핵심 / 모든 그래프 경로의 가중치 값을 더하고 입력한다. / 1번 노드일때 경로들, 2번 노드일때 경로들...
        for g in graph[now]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

    return distance