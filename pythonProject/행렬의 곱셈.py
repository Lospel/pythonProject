def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)) : # 0 1 2
        for j in range(len(arr2[0])) : # 0 1
            for k in range(len(arr1[0])) : # 0 1
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer