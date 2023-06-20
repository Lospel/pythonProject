import re
def solution(phone_number):
    return re.sub('\d(?=\d{4})','*', phone_number) # \d 숫자이지만 (?=\d{4}) 4길이의 숫자는 제외해서 '*' 로 re.sub == replace 해줘