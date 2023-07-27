def solution(prices):
    stack = []
    size = len(prices)
    answer = [0] * size
    for i in range(size):
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)

    for i in stack:
        answer[i] = size - 1 - i

    return answer

# 데이터 수가 적을 경우
def solution2(prices):
    size = len(prices)
    answer = [0] * size
    for i in range(size):
        for j in range(i+1, size):
            if prices[i] <= prices[j]: answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer