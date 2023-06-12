def solution(n):
    answer = []
    dx = [0,1,-1] # 기준점, 아래로, 위로
    dy = [1,0,-1] # 기준점(위에서 시작), 아래로, 위로(좌측 대각선)
    snail = [[0] * i for i in range(1, n+1)] #리스트 컴프리헨션으로 2차원 배열 만듬 0, 00, 000 ...
    x = y = angle = 0
    cnt = 1
    size = n * (n + 1) // 2 # 정수형 값이 나오는 연산자(나누기)

    while cnt <= size:
        snail[y][x] = cnt # 삼각형 형태로 2차원 배열이 배치되도록 y x 로 배열을 만듬
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1

        if 0 <= ny < n and 0 <= nx <= ny and snail[ny][nx] == 0:
            y, x = ny, nx
        else :
            angle = (angle + 1) % 3
            y += dy[angle]
            x += dx[angle]
    answer = [i for j in snail for i in j]
    return answer