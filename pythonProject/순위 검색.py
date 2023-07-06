def solution2(info, query): # 시간복잡도 O(n**2)
    data = [i.split() for i in info]
    queries = []

    for q in query :
        q = q.split()
        for i in range(3) :
            q.remove('and')
        queries.append(q)

    answer = [0] * len(query)

    for i in range(len(queries)):
        q = queries[i]
        for info in data:
            for j in range(5):
                if q[j] == '-':
                    continue
                elif j == 4 and int(info[j]) >= int(q[j]):
                    answer[i] += 1
                elif info[j] != q[j]:
                    break

    return answer

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left
def solution(info, query):
    answer = []
    people = defaultdict(list)

    for i in info :
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)

        for j in range(4):
            candi = list(combinations(person,j))
            for c in candi:
                people[''.join(c)].append(score)

    for i in people: people[i].sort()

    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ','').replace('-', '') # from re import sub key = sub('[ \-]|and', '', key)
        answer.append(len(people[key]) - bisect_left(people[key], score)) # 최대 인원수 - 하한선

    return answer