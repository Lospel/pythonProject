def solution(genres, plays):
    answer = []

    info = {} # 장르별 순번, 재생수
    gens = {} # 장르별 전체 재생수

    for idx, (gen, play) in enumerate(zip(genres, plays)):
        # (0, ('classic', 500))
        if gen not in info:
            info[gen] = [(idx, play)]
        else :
            info[gen].append((idx, play))
        # {'classic': [(0, 500), (2, 150)], 'pop': [(1, 600)]}
        gens[gen] = gens.get(gen, 0) + play

    for (gen, _) in sorted(gens.items(),key=lambda x:x[1], reverse=True):
        # pop 3100
        # classic 1450
        for (idx, _) in sorted(info[gen], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)

    return answer