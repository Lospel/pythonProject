from collections import defaultdict

def dfs(graph, path, visit):
    if path:
        to = path[-1]

        if graph[to] :
            path.append(graph[to].pop(0)) # 큐 형식
            # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'] defaultdict(<class 'list'>, {'ICN': [], 'SFO': [], 'ATL': []})
        else:
            visit.append(path.pop()) # 스택 형식
            #['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']

        dfs(graph, path, visit)

    return visit[::-1] # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)
        # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']})

    for key in graph.keys():
        graph[key].sort()
        # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']})

    return dfs(graph, ["ICN"], [])