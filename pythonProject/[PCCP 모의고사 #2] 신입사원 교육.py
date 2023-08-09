from heapq import heapify, heappop as pop, heappush as push
def solution(ability, number):
    heapify(ability) # 최소값 힙 정렬

    for i in range(number):
        a, b = pop(ability), pop(ability)
        push(ability, a+b)
        push(ability, a+b)

    return sum(ability)