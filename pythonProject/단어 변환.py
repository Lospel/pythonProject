from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])
    visited = [0] * len(words)

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                if sum(x != y for x, y in zip(word, words[i])) == 1: # 각 단어별 틀린 갯수가 1나일 경우
                    q.append([words[i], cnt + 1])
                    visited[i] = 1
    return 0