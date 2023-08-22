def solution(n, s):
    if s < n:
        return [-1]

    # 각 원소의 곱이 최대가 되는 집합 == {몫, 나머지} 값 중에서 몫이 가장 큰 값
    x, y = divmod(s, n)
    answer = [x] * n

    # 이후 두번째 배열부터 나머지 값을 더해주면 최대값 집합이 됨. 나머지가 0이면 계산 x
    for i in range(y):
        answer[i] += 1

    return sorted(answer)

# stack을 활용한 집합 계산
def solution2(n, s):
    answer = []
    if s // n == 0:
        return [-1]

    while n >= 1:
        answer.append(s // n)
        s -= s // n
        n -= 1

    return answer