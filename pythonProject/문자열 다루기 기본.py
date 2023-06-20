import re
def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$",s)) # ^: 시작, \d : 숫자, {4} : 길이, $ : 종료
def solution2(s):
    return len(s) in {4, 6} and bool(re.match('^[0-9]*$', s)) # [0-9] : 0~9 , * : 반복, re.match(x,y) : y에서 x를 찾고 일치하는 값 반환. 없으면 none 반환

def solution3(s):
    if s.isdigit():
        return True
    answer = False
    return answer