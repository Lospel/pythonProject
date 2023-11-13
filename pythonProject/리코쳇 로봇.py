from collections import *


def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    len_board = len(board)
    flen_board = len(board[0])
    diff = [[10e+09 for _ in range(flen_board)] for _ in range(len_board)]

    for i in range(len_board):
        for j in range(flen_board):
            if board[i][j] == "R":
                q.append((i, j, 0))
                diff[i][j] = 0
        if q:
            break

    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x
            ny = y

            while (0 <= nx + dx[i] < len_board and 0 <= ny + dy[i] < flen_board) and (
                    board[nx + dx[i]][ny + dy[i]] != "D"):
                nx += dx[i]
                ny += dy[i]

            if diff[nx][ny] > z + 1:
                diff[nx][ny] = z + 1
                q.append((nx, ny, z + 1))

        if board[x][y] == "G":
            return z

    return -1