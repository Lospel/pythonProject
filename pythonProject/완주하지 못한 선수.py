def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        if answer[k]:
            return k
    return answer[-1]

def solution2(participant, completion):
    value = 0
    answer = {}
    for part in participant:
        answer[hash(part)] = part
        value += int(hash(part))
    for comp in completion:
        value -= int(hash(comp))
    return answer[value]