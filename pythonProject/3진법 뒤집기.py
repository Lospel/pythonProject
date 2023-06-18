def solution(n):
    if n == 0 : return '0'
    nums = []
    while n:
        n, digit = divmod(n, 3) # divmod(x, y)는 x를 y로 나눈 (값, 나머지) 이다.
        nums.append(str(digit)) # 나머지 값을 먼저 append하기 때문에 실제 3진수는 거꾸로 입력됨
        threeAnswer = ''.join(reversed(nums)) # 뒤집어서 정확한 3진수 값으로 입력함
    answer = int(threeAnswer[::-1],3) # 값을 뒤집고 3진수를 10진수로 변환함.
    return answer