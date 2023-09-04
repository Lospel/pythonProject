def solution(n, t, m, timetable):
    answer = "09:00"
    # 모든 시간을 분으로 환산
    crewTime = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    # 버스 도착 시간을 설정, 540 + t*0..n-1
    busTime = [9 * 60 + t * i for i in range(n)]

    # 다음에 버스에 오를 크루의 인덱스
    crewIndex = 0
    for bt in busTime:
        # 버스에 타는 크루 수
        cnt = 0
        # 버스 공간이 남으면서, 현재 크루보다 남은 크루가 더 많고, 현재 크루가 버스 도착 시간 전에 도착했다.
        while cnt < m and crewIndex < len(crewTime) and crewTime[crewIndex] <= bt:
            crewIndex += 1
            cnt += 1
        # 버스 자리가 남으면, 출발 시간에 맞춰서 도착
        if cnt < m:
            answer = bt
        # 아니라면 최종 크루보다 1분 일찍 도착
        else:
            answer = crewTime[crewIndex - 1] - 1

    # zfill(2) == 01 ~ 99, zfill(3) == 001 ~ 999
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)