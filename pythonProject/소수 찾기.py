from itertools import permutations

def solution(numbers):
    answer = []
    numbers = list(numbers)
    num = []

    for i in range(1, len(numbers) + 1):
        num.append(list(permutations(numbers, i)))  # 튜플 형식의 순열 값을 리스트 형식으로 등록함. permutations(값, 형식)

    num = [int(''.join(y)) for x in num for y in x] # 기존 값이 문자열로 들어옴. 배열로 하나씩 값을 뜯은 다음, 해당 배열의 값을 다시 나누어 join하여 하나의 문자로 만든 후 int 형식으로 변환함

    for i in num:
        if checkPrime(i):
            answer.append(i)

    return len(set(answer)) # 중복값을 제거한 값의 길이를 반환함.


# 소수 확인, 루트n 값 안에 소수를 판별할 수 있음
def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True