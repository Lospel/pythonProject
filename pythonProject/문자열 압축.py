def solution(s):
    answer = len(s)
    for x in range(1, len(s)//2 + 1) : # s 길이의 최소값이 1이므로 2로 나누면 값이 0이 나오므로 + 1, 또한 이상에서 미만까지 범위이기 때문이다.
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0, len(s) + 1, x) : # len(s) +1은 마지막 값으로 공백을 넣기 위함
            temp = s[i:i + x] # i 이상 i+x 미만
            if comp == temp : cnt += 1
            elif comp != temp:
                comp_len += len(temp)
                if cnt > 1 : comp_len += len(str(cnt)) # cnt 값이 1자릿수면 1, 2자릿수면 2... 왜? 출력시 2a2ba3c 인데 2자릿수면 12a2ba3c로 1자리가 추가되기 때문.
                cnt = 1
                comp = temp
        answer = min(answer, comp_len)
    return answer