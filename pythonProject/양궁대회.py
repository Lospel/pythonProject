# 중복조합 방식
from itertools import combinations_with_replacement as cwr
def solution(n, info):
    answer = [-1]
    max_gap = -1

    # 라이온이 쏜 화살의 점수 가능성 중복조합
    for shot in cwr(range(11), n):
        case = [0] * 11
        for i in shot: # 0 ~ 10개의 중복조합 배열, 오름차순으로 배열됨
            case[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == case[idx] == 0:
                continue
            elif info[idx] >= case[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx
        # 가장 큰 차이가 나는 값을 가진 중복조합이 answer에 출력됨
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = case

    return answer

# DFS 방식
def compare(current, before):
    for idx in range(10, 0, -1):
        if current[idx] > before[idx]:
            return True
        elif current[idx] < before[idx]:
            return False

def calc(lion, apeach):
    res = 0
    for i in range(len(lion)):
        if apeach[i] < lion[i]:
            res += 10 - i
        elif apeach[i] > lion[i]:
            res -= 10 - i
    return res

def dfs(info, idx, case, choose, n):

    # 화살을 다 썼거나, 점수 과녁 10개를 모두 돌아보고 남았을때
    if n < 0 or idx == 11:
        return

    # 화살이 남았는데, 점수 과녁을 모두 돌아봤을때
    if idx == 10 and n >= 0:
        current = [*choose, n]
        total = calc(current, info)
        # 초기에 라이언은 값이 없으므로, 모든 값이 아파치 값으로 리턴함
        if total > case[0]:
            case[0] = total # 4
            case[1] = current # [3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif total == case[0] and compare(current, case[1]):
            case[1] = current
    # 어피치의 화살 개수보다 한발 더 많이 쐈을 때에 점수
    dfs(info, idx + 1, case, [*choose, info[idx] + 1] , n-(info[idx]+1))

    # 화살을 아끼고 다른 곳에 쐈을 때에 점수
    dfs(info, idx +1, case, [*choose, 0], n)

def solution2(n, info):
    answer = [0, [0] * 11]

    dfs(info, 0, answer, [], n)

    return [-1] if not answer[0] else answer[1]