def back(gen, x):
    child = ["RR", "Rr", "Rr", "rr"]
    if gen == 1:
        return "Rr"
    # n 세대 p값을 4개로 나누어 몫은 부모, 나머지는 자식의 형질 리턴.
    parent = back(gen - 1, x // 4)
    if parent == "Rr":
        return child[x % 4]
    else:
        return parent  # RR, rr

def solution(queries):
    answer = []

    for query in queries:
        n, p = query
        result = back(n, p - 1)
        answer.append(result)

    return answer