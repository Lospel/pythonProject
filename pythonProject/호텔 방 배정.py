import sys
sys.setrecursionlimit(2000)

def find_emptyroom(chk, rooms):
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    empty = find_emptyroom(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty


def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num, rooms)
    return list(rooms)

"""
{1: 2}
{1: 2, 3: 4}
{1: 2, 3: 4, 4: 5}
{1: 3, 3: 4, 4: 5, 2: 3}
{1: 3, 3: 6, 4: 6, 2: 3, 5: 6}
{1: 7, 3: 7, 4: 6, 2: 3, 5: 6, 6: 7}
"""