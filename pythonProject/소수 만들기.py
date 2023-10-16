import itertools as it

def solution(nums):
    answer = 0

    it_nums = it.combinations(nums, 3)

    for i in it_nums:
        decimal = 0
        for j in i:
            decimal += j
        if decimal_check(decimal):
            answer += 1

    return answer


def decimal_check(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True