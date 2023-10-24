import math

def solution(n, stations, w):
    answer = 0
    w_range = w * 2 + 1
    start = 1

    for x in stations:
        end = x - w
        if end < 2:
            start = x + w + 1
        else:
            house = end - start
            start = x + w + 1
            answer += math.ceil(house / w_range)

    if x + w < n:
        start = x + w
        house = n - start
        answer += math.ceil(house / w_range)

    return answer