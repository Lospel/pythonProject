def solution(s):
    data = s[2:-2].split("},{")
    data = sorted(data, key=lambda x:len(x)) # 길이별 오름차순 정렬. lambda <표현식> : <표현식을 이용한 연산>
    answer = []
    for item in data :
        item = list(map(int,item.split(",")))
        for value in item :
            if value not in answer :
                answer.append(value)
    return answer

def solution2(s):
    answer = {} # 딕셔너리 사용
    s = sorted(s[2:-2].split("},{"), key=len)
    for tuples in s :
        elements = tuples.split(',')
        for element in elements :
            number = int(element)
            if number not in answer :
                answer[number] = 1 # 딕셔너리 키 사용 answer[키] = 값
    return list(answer) # 딕셔너리 값이 배정된 키만 배열로 리턴됨