def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

def solution2(strings, n):
    return sorted(strings, key=lambda x: x[n] + x)

def solution3(strings, n):
    return sorted(strings, key=lambda x: (x[n] , x))