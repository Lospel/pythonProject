def solution(a):
    if len(a) == 1:
        return 1

    answer = 0

    left = [a[0] for _ in range(len(a))]
    right = [a[-1] for _ in range(len(a))]

    for i in range(1, len(a)):
        left[i] = min(left[i - 1], a[i])

    for i in range(1, len(a)):
        right[i] = min(right[i - 1], a[len(a) - i - 1])

    right.reverse()
    for i in range(len(a)):
        if left[i] < a[i] and right[i] < a[i]:
            answer += 1

    return len(a) - answer