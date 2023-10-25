def solution(picks, minerals):
    answer = 0
    sum_picks = 0
    for i in picks:
        sum_picks += i

    num = sum_picks * 5
    if len(minerals) > sum_picks:
        minerals = minerals[:num]

    new_minerals = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1

    new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    for i in new_minerals:
        dia, iron, stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * dia) + (5 * iron) + stone
                break

    return answer