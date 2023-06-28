from itertools import permutations
import re


def toPostFix(tokens, priority):
    stack = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)  # 숫자는 postfix 쌓는다.
        else:
            if not stack:
                stack.append(token)  # stack 비어 있으면 쌓는다.
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(token)
    while stack:
        postfix.append(stack.pop())

    return postfix


def calc(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
        num1 = stack.pop()
        num2 = stack.pop()

        if token == '*':
            stack.append(num2 * num1)
        elif token == '+':
            stack.append(num2 + num1)
        else:
            stack.append(num2 - num1)

    return stack.pop()


def solution(expression):
    answer = 0
    tokens = re.split('([-+*])', expression)
    operators = ['+', '-', '*']

    for i in map(list, permutations(operators)):
        priority = {o: p for p, o in enumerate(list(i))}  # 순열로 입력된 순서에 key:value 형태로 입력하여, 우선 순위를 설정함
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))

    return answer