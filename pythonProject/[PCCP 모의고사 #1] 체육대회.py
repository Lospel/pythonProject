# 조합, 순열
from itertools import combinations, permutations
def solution(ability):
    answer = 0
    people, event_size = len(ability), len(ability[0])
    scores = [i for i in range(people)]
    events = [i for i in range(event_size)]

    for i in combinations(scores, event_size):
        for j in permutations(events, event_size):
            power = 0
            for k in range(len(j)):
                power += ability[i[k]][j[k]]
            answer = max(power, answer)

    return answer

# DFS + 동적 프로그래밍
def dfs(depth, selected, ability, dp):
    students, sports = len(ability), len(ability[0])
    if depth == sports:
        return 0

    if not dp[selected]:
        for student in range(students):
            if selected & (1 << student):
                continue
            current = ability[student][depth]
            select = dfs(depth + 1, selected | (1<<student), ability, dp)
            dp[selected] = max(current + select, dp[selected])
    return dp[selected]

def solution2(ability):
    dp = [0] * (1<<len(ability))
    return dfs(0, 0,ability, dp)