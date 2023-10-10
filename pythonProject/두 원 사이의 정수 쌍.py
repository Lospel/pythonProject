# 타원 안의 점 구하기 공식: z**2 = y**2 - x**2 (y: 반지름, x: 선택한 값, z: 구하는 점의 개수)
import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        if i < r1:
            # ceil 반올림 sqrt 루트
            small = math.ceil(math.sqrt(r1 ** 2 - i ** 2))
        else:
            small = 0
        large = int(math.sqrt(r2 ** 2 - i ** 2))
        answer = answer + large - small + 1

    return answer * 4