def solution(s):
    stack = []
    for case in s :
        if stack and stack[-1] == case : stack.pop() # 스택에 값이 있고 마지막 값이 같은지 (stack이 없으면 없는 값을 찾으려고 하기 때문에 범위 오류 발생)
        else: stack.append(case)
    answer = 0 if stack else 1
    return answer