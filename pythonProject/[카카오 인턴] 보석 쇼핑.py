def solution(gems):
    kind = len(set(gems)) # 중복이 제거된 보석대 길이 4
    size = len(gems) # 중복이 허용된 보석대 길이(원본) 8
    answer = [0, size-1] # [0, 7]

    dic = {gems[0]:1} # {'DIA' : 1 }
    start = end = 0

    while end < size : # 0 < 8 -> 7 < 8
        if len(dic) < kind: # 1 < 4 .. 3 < 4
            end += 1
            if end == size: break
            dic[gems[end]] = dic.get(gems[end], 0) + 1 # { 'RUBY' : 1 }
        else: # end == 6, len(dic) == 4 ... len(dic) == 3
            if (end - start + 1) < (answer[1] - answer[0] + 1): # 6 - 0 + 1 < 7 - 0 + 1 ... 6 - 2 + 1 < 6 - 1 + 1
                answer = [start, end] # answer = [0, 6] ... [2, 6]
            if dic[gems[start]] == 1:
                del dic[gems[start]] # 0 값으로 될 경우 지우고 한칸 앞쪽으로 포인트를 옮김
            else:
                dic[gems[start]] -= 1
            start += 1

    # 보석대가 1번부터 시작하므로 값을 +1씩 함.
    answer[0] += 1
    answer[1] += 1

    return answer