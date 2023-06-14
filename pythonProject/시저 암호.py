def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)) :
        if s[i] == ' ' : continue
        corr = ord('A') if s[i].isupper() else ord('a') # ord('A') == 65 ord('a') == 97
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr) # 알파벳 총 갯수 26개 (대소문자 구분x)
    answer = ''.join(s)
    return answer