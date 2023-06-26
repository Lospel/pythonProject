def solution(brown, yellow):
    answer = []
    grid = brown + yellow
    # 최소 길이부터 정사각형까지
    # 정사각형 대각선 길이 = 루트(가로 + 세로) , 직사각형 대각선 길이 = 루트(가로**2 + 세로**2)
    for n in range(3, int(grid**0.5) + 1) :
        if grid % n != 0: continue
        m = grid // n
        if (n-2) * (m-2) == yellow:
            answer = [m, n]
    return answer