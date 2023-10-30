def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    dp1 = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]

    dp1[0], dp1[1] = sticker[0], sticker[0] + dp1[0]
    dp2[0], dp2[1] = 0, sticker[1] + dp2[0]

    for i in range(2, len(sticker)):
        if i == len(sticker) - 1:
            dp2[i] = max(dp2[i - 1], sticker[i] + dp2[i - 2])
        else:
            dp1[i] = max(dp1[i - 1], sticker[i] + dp1[i - 2])
            dp2[i] = max(dp2[i - 1], sticker[i] + dp2[i - 2])

    answer = max(dp1[len(dp1) - 2], dp2[len(dp2) - 1])

    return answer