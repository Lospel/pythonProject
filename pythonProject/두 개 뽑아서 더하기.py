from itertools import combinations
def solution(numbers):
    answer = set()
    selects = list(combinations(numbers, 2))

    for select in selects:
        (a, b) = select
        answer.add(a + b)

    return sorted(answer)

def solution2(numbers):
    return sorted(set(map(sum, combinations(numbers,2))))