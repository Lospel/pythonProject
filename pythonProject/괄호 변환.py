def check(string):
    stack = []

    for bracket in string:
        if bracket == '(':
            stack.append('(')
        elif stack:
            stack.pop()
        else:
            return False
    return True

def dfs(string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not string:
        return string
    close = 0

    for i in range(len(string)):
        if string[i] == '(':
            close += 1
        else:
            close -= 1

        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        if close == 0:
            if check(string[:i+1]): # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. (*함수: 함수를 새로 호출)
                return ''.join([string[:i+1], *dfs(string[i+1:])]) #  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
            else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
                v = ['(', *dfs(string[i+1:]), ')']
                # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
                # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
                # 4-3. ')'를 다시 붙입니다.
                for a in range(1, i): # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
                    if string[a] == '(':
                        v.append(')')
                    else:
                        v.append('(')
                return ''.join(v) # 4-5. 생성된 문자열을 반환합니다.
def solution(p):
    return dfs(p)