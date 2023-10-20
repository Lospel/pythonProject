from collections import deque

def solution(n, words):
    answer = same_check(n, words)
    if answer[0] > 0:
        return answer

    stack = deque(words)
    person = dict()
    for i in range(n):
        person[i] = 0
    cnt = 0

    while stack and len(stack) > 1:
        x = stack.popleft()
        y = stack.popleft()
        if x[-1] == y[0]:
            person[cnt % n] += 1
            stack.appendleft(y)
            cnt += 1
        elif x[-1] != y[0]:
            cnt += 1
            person[cnt % n] += 1
            answer = [cnt % n + 1, person[cnt % n]]
            break

    return answer


def same_check(n, words):
    dic_words = dict()
    person = dict()

    for i in range(n):
        person[i + 1] = 0
    cnt = 0

    for i in words:
        cnt += 1
        dic_words.setdefault(i, 0)
        dic_words[i] += 1
        person[(cnt - 1) % n + 1] += 1
        if dic_words[i] > 1:
            return [(cnt - 1) % n + 1, person[(cnt - 1) % n + 1]]

    return [0, 0]

# def solution(n, words):
#     answer = [0,0]
#     stack = [words[0]]
#     for i in range(1, len(words)):
#         if stack[-1][-1] == words[i][0] and words[i] not in stack:
#             stack.append(words[i])
#         else:
#             answer[0] = (i % n) + 1
#             answer[1] = i // n + 1
#             break
#     return answer