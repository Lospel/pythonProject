from math import factorial # ex) 3! = 3 * 2 * 1
def solution(n, k):
    numbers = list(range(1, n+1))
    answer = []
    k -= 1

    while numbers:
        idx, k = divmod(k, factorial(len(numbers) - 1)) # k 값을 팩토리얼 값으로 나눈 몫과 나머지로 튜플을 만듬
        answer.append(numbers.pop(idx))

    return answer