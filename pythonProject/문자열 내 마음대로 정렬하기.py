def solution(strings, n): # 특정 단어 순으로 정렬
    return sorted(sorted(strings), key=lambda x: x[n])

def solution2(strings, n): # 합쳐서 정렬
    return sorted(strings, key=lambda x: x[n] + x)

def solution3(strings, n): #튜플 형식 정렬
    return sorted(strings, key=lambda x: (x[n] , x))