def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for x in A:
        if B[0] > x:
            answer += 1
            del B[0]
        else:
            continue
    return answer