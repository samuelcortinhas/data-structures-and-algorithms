def kadanes(arr):
    # Time O(n), Memory O(1)
    curr_sum = 0
    max_sum = arr[0]
    for n in arr:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


arr = [4, -1, 2, -7, 3, 4]
print(kadanes(arr))
