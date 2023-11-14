def solution(s):
    list_s = s.split(" ")
    lower_s = [i.capitalize() for i in list_s]
    answer = ' '.join(lower_s)
    return answer