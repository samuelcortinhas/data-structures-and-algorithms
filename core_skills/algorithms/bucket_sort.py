def bucket_sort(arr, k):
    # Time O(n + k), Memory O(n) where k = #buckets
    # Assume data lies in [0, 1, 2, ..., k - 1]
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    i = 0
    for n in range(k):
        for _ in range(counts[n]):
            arr[i] = n
            i += 1

    return arr


arr = [4, 1, 3, 0, 2, 3, 4]
print(bucket_sort(arr, 5))
