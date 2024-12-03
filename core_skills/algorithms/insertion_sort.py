def insertion_sort(arr):
    # Time O(n^2), Memory O(1), stable
    for i in range(len(arr)):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp
            j -= 1
    return arr


if __name__ == "__main__":
    arr = [8, 1, 7, 8, 4, 2, 7, 1, 8, 3]
    print(insertion_sort(arr))
