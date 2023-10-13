def solution(plans):
    answer = []
    lenght = len(plans)
    for i in range(lenght):
        a, b = map(int, plans[i][1].split(":"))
        time = a * 60 + b
        plans[i][1] = time
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    stack = []

    for i in range(lenght):
        if i == lenght - 1:
            stack.append(plans[i])
            break

        name, start, playtime = plans[i]
        next_name, next_start, next_playtime = plans[i + 1]

        if start + playtime <= next_start:
            answer.append(name)
            temp_time = next_start - (start + playtime)

            while temp_time != 0 and stack:
                pre_name, pre_start, pre_playtime = stack.pop()
                if temp_time >= pre_playtime:
                    answer.append(pre_name)
                    temp_time -= pre_playtime
                else:
                    stack.append([pre_name, pre_start, pre_playtime - temp_time])
                    temp_time = 0
        else:
            plans[i][2] = playtime - (next_start - start)
            stack.append(plans[i])

    while stack:
        name, start, playtime = stack.pop()
        answer.append(name)

    return answer