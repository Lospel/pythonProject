# 최소극대화 알고리즘 게임이론
def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    inside = lambda x, y: 0 <= x < n and 0 <= y < m

    def dfs(aloc, bloc, seen, step):
        x, y = aloc if step % 2 == 0 else bloc
        survive, must_lose = False, True
        win_left, lose_left = [], []

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            # (nx, ny) not in seen : A와 B가 모두 움직이지 않은 곳인가
            if inside(nx, ny) and (nx, ny) not in seen and board[nx][ny]:
                survive = True

                # A가 움직이다 B랑 위치가 겹치는 즉시, B가 승리한 결과와 A가 움직인 결과 값을 리턴
                if aloc == bloc:
                    return (True, step + 1)

                # A일 경우, A의 움직임을 기록하고 상대편은 그대로.
                next_step = [[nx,ny], bloc] if step % 2 ==0 else [aloc, [nx, ny]]

                # seen | {(x, y)} == {(1, 0), (0, 2), (1, 2), (0, 0)}
                # 상대 플레이어로 바꿔서 dfs를 진행한다.
                win, left = dfs(*next_step, seen | {(x, y)}, step + 1)

                # 리턴되는 값의 주인은 상대 플레이어이므로 반대로 명시해야한다.
                if win:
                    win_left.append(left)
                else:
                    lose_left.append(left)

                # AND 연산자는 T & T 일 경우만 T이고 나머지는 F이다. 따라서, 현재 플레이어가 한번이라도 진다면 상대 플레이어는 must_lose 값이 F로 나온다.
                must_lose &= win

        # 현재 플레이어가 생존하지 못한 값을 리턴하므로, 이전 dfs 값의 플레이어는 must_lose 가 F가 된다. 따라서, 이전 플레이어의 리턴 값은 T와 최소 패배 턴이 된다.
        if not survive:
            return (False, step)

        # must_lose가 한번도 F가 안된다면 현재 플레이어의 리턴 값이 항상 T이므로, 상대 플레이어는 F와 최대 승리 턴이 리턴된다.
        if must_lose:
            return (False, max(win_left))

        return (True, min(lose_left))

    return dfs(aloc, bloc, set(), 0)[1]