def solution(A, B):
    answer = 0
    stack_A = [i for i in A]
    stack_A.sort()
    stack_B = [i for i in B]
    stack_B.sort(reverse=True)

    while (stack_A):
        x = stack_A.pop()
        y = stack_B.pop()
        answer += x * y
    return answer