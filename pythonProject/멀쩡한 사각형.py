import math

def solution(w,h):
    # math.gcd(x, y) x, y 의 최대공약수
    x = math.gcd(w, h)
    answer = (w * h) - (w + h - x)
    return answer