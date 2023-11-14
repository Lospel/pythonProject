def solution(s):
    list_s = s.split(" ")
    int_s = [int(i) for i in list_s]
    answer = str(min(int_s)) + " " + str(max(int_s))
    return answer