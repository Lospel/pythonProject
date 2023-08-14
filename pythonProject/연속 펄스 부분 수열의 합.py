# 시간 초과
def solution2(sequence):
    answer = 0
    pulsePlus = [1, -1]
    pulseMinus = [-1, 1]

    sequenceP = []
    sequenceM = []

    for i in range(len(sequence)):
        sequenceP.append(sequence[i] * pulsePlus[i % 2])
        sequenceM.append(sequence[i] * pulseMinus[i % 2])

    for i in range(len(sequence)):
        for j in range(i, len(sequence) + 1):
            pP = 0
            pM = 0

            for x in sequenceP[i:j]:
                pP += x
            for x in sequenceM[i:j]:
                pM += x

            answer = max(pP, pM, answer)

    return answer

# 동적 프로그래밍
def solution(sequence):
    pulse = lambda x: 1 if x % 2 else -1 # -1, 1, -1
    sequence = [pulse(idx) * sequence[idx] for idx in range(len(sequence))]

    # 초기값 설정, dp[(최솟값, 최댓값),...]
    dp = [[0, 0] for _ in range(len(sequence))]
    dp[0] = [sequence[0], sequence[0]]

    for i in range(1, len(sequence)):
        # 1개 배열값과 이전 배열까지의 값을 더하고 비교
        dp[i][0] = min(sequence[i], sequence[i] + dp[i - 1][0])
        dp[i][1] = max(sequence[i], sequence[i] + dp[i - 1][1])

    min_val = min(map(min, dp))
    max_val = max(map(max, dp))

    return max(abs(min_val), abs(max_val)) # 절대값으로 비교함으로 펄스 수열의 반대 방향과 동일한 결과가 나옴