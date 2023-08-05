def change(n, k):
    ret = []
    # k 진수로 변환하려면 n 값을 k로 몫과 나머지로 계속 나눈 뒤, 반대로 출력하면 됨
    while n > 0:
        n, x =divmod(n, k)
        ret.append(str(x))
    return ''.join(ret[::-1])

def is_prime(n):
    if n < 2:
        return False
    # 소수는 약수 특징상, 루트값 밑으로 판단이 가능함.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = change(n, k)

    for n in k_num.split('0'):
        if not n:
            continue
        if is_prime(int(n)):
            answer += 1

    return answer