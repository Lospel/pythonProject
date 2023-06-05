import heapq

def solution(alp, cop, problems):
    answer = 0
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    dp = {(alp, cop): 0}
    q = [(0, (alp, cop))]

    def put(count, key):
        if key not in dp or count < dp[key]:
            dp[key] = count
            heapq.heappush(q, (count, key))

    alpMax = max(i[0] for i in problems)
    copMax = max(i[1] for i in problems)

    while q[0][1][0] < alpMax or q[0][1][1] < copMax:
        count, (alp2, cop2) = heapq.heappop(q)
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp2 >= alp_req and cop2 >= cop_req:
                put(count + cost, (min(alp2 + alp_rwd, 150), min(cop2 + cop_rwd, 150))) # 알고력과 코딩력이 150 제한을 못넘기게 만듬

    answer = q[0][0]
    return answer