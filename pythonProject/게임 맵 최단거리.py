from collections import deque
def solution(maps):
    width, height = len(maps[0]), len(maps)
    visited = [[0] * width for x in range(height)]
    visited[0][0] = 1

    next_path = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for path in next_path:
            nx = x + path[0]
            ny = y + path[1]

            # 배열상 x 값은 height, y 값은 width 와 비교해야 한다.
            if (nx >= 0) and (ny >= 0) and (nx < height) and (ny < width):
                if (maps[x][y] == 1 and visited[nx][ny] == 0):
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return visited[height - 1][width - 1] or -1