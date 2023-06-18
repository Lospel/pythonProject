def solution(s):
    change, zero = 0, 0
    while s != '1':
        change += 1
        num = s.count('1') # 0을 제거한 값의 길이 == 1의 개수 합
        zero += len(s) - num # 값에서 1의 개수를 제거한 길이 == 0의 개수
        s = bin(num)[2:] # 10진수를 2진수로 변환하되 0b 값은 제거하고 입력해야됨. 그래야 온전한 2진수 값이 입력됨.
    answer = [change, zero] # 횟수, 제거한 0의 개수
    return answer