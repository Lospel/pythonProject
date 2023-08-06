from collections import defaultdict
def solution(info, edges):
    answer = []
    graph = defaultdict(list)

    for parent, child in edges:
        graph[parent].append(child)

    def dfs(current, sheep, wolf, possible_path):
        sheep += info[current] ^ 1 # 0 이면 1, 1이면 0
        wolf += info[current] # 0이면 0, 1이면 1

        if sheep <= wolf:
            return
        if sheep > wolf: # 1 > 0
            answer.append(sheep)
            for upcoming in possible_path: # 자식 노드 [1, 8]
                # grapsh.get(값, 타입)
                temp = set(graph.get(upcoming, [])) # 자식 노드의 자식 {2, 4}, {9, 7}
                # {1, 8, 7, 9}
                possible_path |= temp # | 비트 or , |= 비트 or 연산 후 a 값에 결과 값을 할당함
                possible_path -= set([upcoming])
                dfs(upcoming, sheep, wolf, possible_path)
                possible_path |= set([upcoming])
                possible_path -= temp

    dfs(0,0,0,set(graph.get(0))) # 중복 없는 부모 노드 0의 자식값
    return max(answer)

def solution2(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []

    def dfs(sheep, wolves):
        if sheep > wolves:
            answer.append(sheep)
        else:
            return

        for edge in edges:
            parent, child = edge
            wolf = info[child] == 1

            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep + (not wolf), wolves + wolf)
                visited[child] = 0

    dfs(1, 0)
    return max(answer)