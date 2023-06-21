def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

def hanoi(n, one, two, three, answer): # 2, 1, 2, 3
    if n == 1:
        return answer.append([one, three])
    hanoi(n-1, one, three, two, answer) # 1, 1, 3, 2 처음값
    answer.append([one, three]) # 중간값
    hanoi(n-1, two, one, three, answer) # 1, 2, 1, 3 마지막값