def kadanes(arr):
    # Time O(n), Memory O(1)
    curr_sum = 0
    max_sum = float("-inf")
    for n in arr:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


def kadanes_sliding_window(arr):
    # Time O(n), Memory O(1)
    # Returns indexes of subarray boundaries
    curr_sum = 0
    max_sum = float("-inf")
    i, j = 0, 0
    res_i, res_j = 0, 0

    while j < len(arr):
        if curr_sum < 0:
            curr_sum = 0
            i = j
        curr_sum += arr[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
            res_i, res_j = i, j
        j += 1
    return res_i, res_j


arr = [4, -1, 2, -7, 3, 4]
print(kadanes(arr))
print(kadanes_sliding_window(arr))
