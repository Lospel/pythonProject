def solution(citations):
    answer = 0
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx :
            return len(citations)-idx
    return answer

def solution2(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)