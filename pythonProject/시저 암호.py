def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)) :
        if s[i] == ' ' : continue
        corr = ord('A') if s[i].isupper() else ord('a') # 예) A > B ? a : b
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)
    answer = ''.join(s)
    return answer