def solution(target):
    return dfs(target, 0, 0)


def dfs(target, dart, sum):
    if target <= 20:
        dart += 1
        sum += 1
        return [dart, sum]

    elif target < 50:
        dart += 1
        if target % 3 == 0:
            return [dart, sum]
        else:
            dart += 1
            sum +=1
            return [dart, sum]

    else:
        Bool = target // 50
        target = target % 50
        dart += Bool
        sum += Bool
        return dfs(target, dart, sum)