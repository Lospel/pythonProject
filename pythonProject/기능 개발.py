def solution(progresses, speeds):
    answer = []

    for progress, speed in zip(progresses, speeds):
        left = -((progress - 100) // speed)
        if not answer or answer[-1][0] < left:
            answer.append([left, 1])
        else: answer[-1][1] += 1

    return [a[1] for a in answer]

def solution2(progresses, speeds):
    answer = []
    # 한바퀴 = 하루
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0 : answer.append(cnt)

    return answer