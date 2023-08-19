def solution2(n, works):
    if sum(works) <= n:
        return 0

    for i in range(n):
        works.sort(reverse=True)
        works[0] = works[0] - 1

    answer = [x ** 2 for x in works]

    return sum(answer)

from heapq import heappush, heappop, heapify

def solution(n, works):
    if sum(works) <= n:
        return 0
    # 힙 구조는 우선순위 큐 구조로 정렬 즉, 자동으로 오름차순 정렬됨
    works = [-x for x in works]
    heapify(works)

    for i in range(n):
        x = heappop(works)
        x += 1
        heappush(works, x)

    return sum([x ** 2 for x in works]) # 제곱하면 음수는 양수값으로 변환됨