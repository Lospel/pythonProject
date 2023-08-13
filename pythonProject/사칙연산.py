# 동적프로그래밍 https://www.ai-bio.info/programmers/1843
# 아이디어 및 해결 방법
# 다이나믹 프로그래밍으로 해결 가능합니다.
# 중요한 아이디어는, 최댓값을 구하기 위해서는 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 합니다.
# 따라서 i번째 수부터 j번째 수까지, 여러 가지 가능한 연산 결과 중 (1) 최댓값과 (2) 최솟값을 각각 저장해두어야 합니다.
# 편의상 (i, j) 튜플을 키로 갖는 딕셔너리로 메모이제이션 합니다.
# M[(i, j)] : nums[i] 부터 nums[j] 까지 연산했을 때 나올 수 있는 최댓값
# m[(i, j)] : nums[i] 부터 nums[j] 까지 연산했을 떄 나올 수 있는 최솟값
# DP를 위한 관계식은 아래와 같습니다.
# i < k <= j 인 k를 생각하여 i~j 구간이 i~k-1, k~j 의 두 구간으로 나뉜다고 하자.
# 이 때, op[k-1]의 종류에 따라서 M[(i, j)]와 m[(i, j)]계산을 위해 기억해둘 값이 달라진다.
# op[k-1]이 + 인 경우,
# 최댓값을 위해서는 M[(i, k-1)] + M[(k, j)]를 기억해둔다. (큰 값과 큰 값을 더함)
# 최솟값을 위해서는 m[(i, k-1)] + m[(k, j)]를 기억해둔다. (작은 값과 작은 값을 더함)
# op[k-1]이 -인 경우,
# 최댓값을 위해서는 M[(i, k-1)] - m[(k, j)]를 기억해둔다. (큰 값에서 작은 값을 뺌)
# 최솟값을 위해서는 m[(i, k-1)] - M[(k, j)]를 기억해둔다. (작은 값에서 큰 값을 뺌)
# 이제 기억해둔 값들을 가지고, 각각 그 값들의 최댓값, 최솟값을 M[(i, j)]와 m[(i, j)]에 할당하면 된다. 이를 반복한다.
def solution(arr):
    M, m = {}, {}
    nums = [int(x) for x in arr[::2]] # 문자열을 숫자로
    ops = [x for x in arr[1::2]] # 기호만

    for i in range(len(nums)): # 0 ~ 3
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]

    for d in range(1, len(nums)): # 1 ~ 3
        for i in range(len(nums)): # 0 ~ 3
            j = i + d # 0 + 1
            if j >= len(nums): # j >= 4
                continue

            maxCandidates, minCandidates = [], []
            for k in range(i + 1, j + 1): # 0+1 , 1+1
                if ops[k - 1] == '-': # 1-1
                    mx = M[(i, k - 1)] - m[(k, j)] # mx = 1 - 3
                    mn = m[(i, k - 1)] - M[(k, j)]
                    maxCandidates.append(mx)
                    minCandidates.append(mn)
                else:
                    mx = M[(i, k - 1)] + M[(k, j)]
                    mn = m[(i, k - 1)] + m[(k, j)]
                    maxCandidates.append(mx)
                    minCandidates.append(mn)

            M[(i, j)] = max(maxCandidates)
            m[(i, j)] = min(minCandidates)

    return M[(0, len(nums) - 1)]