def solution(places):
    answer = [check(place) for place in places]
    return answer

def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != 'P' :
                continue

            isNotEndRow = idx_row != 4
            isNotEndCol = idx_col != 4
            isNotFirstCol = idx_col != 0
            isBeforeThirdRow = idx_row < 3 # 5줄이므로 3줄까지만 2칸 이상 거리를 확인할 수 있음
            isBeforeThirdCol = idx_col < 3

            if isNotEndRow : # 마지막 행 전까지 아래로 내려가면서 체크
                Down = place[idx_row + 1][idx_col]
                if Down == 'P' : return 0
                if isBeforeThirdRow :
                    TwoTimesDown = place[idx_row + 2][idx_col]
                    if TwoTimesDown == 'P' and Down != 'X' : return 0
                if isNotEndCol :
                    Right = place[idx_row][idx_col + 1]
                    RightDown = place[idx_row + 1][idx_col + 1]
                    if RightDown == 'P' and (Down != 'X' or Right != 'X') : return 0
                if isNotFirstCol :
                    Left = place[idx_row][idx_col - 1]
                    LeftDown = place[idx_row + 1][idx_col - 1]
                    if LeftDown == 'P' and (Down != 'X' or Left != 'X') : return 0

            if isNotEndCol : # 마지막 열 전까지 오른쪽으로 가면서 체크
                Right = place[idx_row][idx_col + 1]
                if Right == 'P' : return 0
                if isBeforeThirdCol :
                    TwoTimesRight = place[idx_row][idx_col + 2]
                    if TwoTimesRight == 'P' and Right != 'X' : return 0
    return 1