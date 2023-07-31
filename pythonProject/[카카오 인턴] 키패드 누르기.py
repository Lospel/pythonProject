def dist(target, pos):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])


def solution(numbers, hand):
    pattern = {'L': (1, 4, 7), 'R': (3, 6, 9)}
    pos = {'L': [0, 3], 'R': [2, 3]}  # {(1, 4, 7, *), (2, 5, 8, 9), (3, 6, 9, #)}
    result = []

    def press(which, coord):
        result.append(which)
        pos[which] = coord

    for number in numbers:
        choose = 'L'
        target = [0, (number - 1) // 3]  # 4를 누르면 (0, 1) 배열값

        if number in pattern['L']:
            pass
        elif number in pattern['R']:
            choose = 'R'
            # target = [2, (number - 1) // 3] # target의 첫번째 값은 없어도 결과는 동일. 왜냐하면 2 - 1 과 0 - 1 의 절대값은 동일하기 때문.
        else:
            target = [1, 3 if number == 0 else (number - 1) // 3]  # 2 5 8 0
            left = dist(target, pos['L'])
            right = dist(target, pos['R'])

            if right < left:
                choose = 'R'
            elif right == left and hand == 'right':
                choose = 'R'

        press(choose, target)

    return ''.join(result)
