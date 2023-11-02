# 1차
def solution(players, callings):
    for i in callings:
        idx = players.index(i)
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players

# 2차
def solution(players, callings):

    stack = {player: i for i, player in enumerate(players)}
    for i in callings:
        idx = stack[i]
        stack[i] -= 1
        stack[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players