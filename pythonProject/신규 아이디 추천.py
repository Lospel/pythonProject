def solution(new_id):
    answer = new_id.lower()
    filtered = []

    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'): # 알파뱃, 숫자, 특정 문자
            filtered.append(c)
    answer = ''.join(filtered)

    while '..' in answer :
        answer = answer.replace('..', '.')

    answer = answer.strip('.') # strip 양 옆으로 특정 문자열 제거

    if answer == '' : answer = 'a'
    if len(answer) > 15 : answer = answer[:15]
    if answer[-1] == '.' : answer = answer[:-1]

    while len(answer) < 3 :
        answer += answer[-1]

    return answer