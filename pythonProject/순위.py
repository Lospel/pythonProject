from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    for i in range(1, n+1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer

def solution2(n, results):
    total = [['????' for i in range(n)] for j in range(n)] # 100 * 100

    for i in range(n):
        total[i][i] = 'SELF' # 대각선은 자기 자신의 그래프이므로 값을 없앰.

    for result in results:
        total[result[0] - 1][result[1] - 1] = "WINS" # 선수 번호는 1번부터 시작하지만 배열은 0번부터 시작하므로, 1씩 번호 값을 뺌.
        total[result[1] - 1][result[0] - 1] = "LOSE"

    # 플로이드-워셜 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == "WINS" and total[k][j] == "WINS":
                    total[i][j] = "WINS"
                elif total[i][k] == "LOSE" and total[k][j] == "LOSE":
                    total[i][j] = "LOSE"

    answer = 0

    for i in total:
        if '????' not in i:
            answer += 1

    return answer