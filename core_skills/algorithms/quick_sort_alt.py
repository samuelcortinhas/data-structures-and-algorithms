def quick_sort(array, left, right):
    if right - left < 1:
        return array

    pivot = right
    swap_count = 0
    for i, x in enumerate(array[left : right + 1]):
        if x <= array[pivot]:
            tmp = array[left + swap_count]
            array[left + swap_count] = x
            array[left + i] = tmp
            swap_count += 1

    array = quick_sort(array, left, left + swap_count - 2)
    array = quick_sort(array, left + swap_count, right)
    return array


arr = [4, 5, 6, 1, 7, 3]
print(quick_sort(arr, 0, len(arr) - 1))
