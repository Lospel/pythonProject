import heapq

def solution(operations):
    answer = [0, 0]
    hq = list()

    for x in operations:
        left = x.split()
        if left[0] == "I":
            heapq.heappush(hq, int(left[1]))
        elif hq:
            if int(left[1]) >= 0:
                hq.remove(max(hq))
            else:
                heapq.heappop(hq)
    if hq:
        answer = [max(hq), min(hq)]

    return answer