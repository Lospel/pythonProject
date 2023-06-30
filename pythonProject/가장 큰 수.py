from functools import cmp_to_key # 임의 정렬 방식

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(lambda x, y : int(x+y) - int(y+x)), reverse=True) # x+y 와 y+x를 비교해서 내림차순으로 정렬
    answer = str(int(''.join(numbers))) # 앞에 0 값을 자동으로 제거하고 다시 문자 형식으로 변환
    return answer

def solution2(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True) # 문자열 * 3 이므로 3번 반복한 값을 비교함, 666 vs 101010 일 경우 일의 자리는 6 vs 1, 이의 자리는 6 vs 0 이므로 정렬시에는 666이 더 큰 값으로 인식함
    result = ''.join(numbers)
    if '0' * len(numbers) == result : return '0'
    return result