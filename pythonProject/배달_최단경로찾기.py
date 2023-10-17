import heapq

def solution(N, road, K):
    graph = [float('inf')] * (N + 1)
    graph[1] = 0
    step = [[] for _ in range(N + 1)]
    for i in road:
        step[i[0]].append([i[2], i[1]])
        step[i[1]].append([i[2], i[0]])
    dfs(graph, step)
    answer = len([i for i in graph if i <= K])
    return answer

def dfs(graph, step):
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in step[node]:
            if cost + c < graph[n]:
                graph[n] = cost + c
                heapq.heappush(heap, [cost + c, n])