def solution(sequence, k):
    answer = []
    n = len(sequence)
    index_sum = 0
    right = 0
    index_len = n

    for left in range(n):
        while index_sum < k and right < n:
            index_sum += sequence[right]
            right += 1
        if index_sum == k and right - 1 - left < index_len:
            answer = [left, right - 1]
            index_len = right - 1 - left

        index_sum -= sequence[left]

    return answer