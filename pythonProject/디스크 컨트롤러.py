from heapq import heappush as push, heappop as pop # 우선순위 큐
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):

        for job in jobs:  # [[0, 3], [1, 9], [2, 6]]
            if start < job[0] <= now:
                push(heap, job[::-1])  # [3, 0]
                print(heap)

        if len(heap) > 0:
            cur = pop(heap)  # [3, 0], [6, 2], [9, 1]
            start = now  # 0, 3, 9
            now += cur[0]  # 3, 9, 18
            answer += now - cur[1]  # 3 - 0 = 3, 3 + 9 - 2 = 10, 10 + 18 - 1 = 27
            i += 1
        else:
            now += 1

    return answer // len(jobs)  # 27 // 3 == 9