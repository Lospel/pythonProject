def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    left = 0

    for target in targets:
        if target[0] >= left:
            answer += 1
            left = target[1]

    return answer