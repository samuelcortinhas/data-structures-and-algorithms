def binary_search(lst, target):
    """
    Assumes list is sorted.
    O(log(n)) time complexity
    O(1) space complexity
    """
    start = 0
    end = len(lst) - 1

    while start <= end:
        midpoint = (start + end) // 2

        if lst[midpoint] == target:
            return midpoint

        elif lst[midpoint] < target:
            start = midpoint + 1

        else:
            end = midpoint - 1


if __name__ == "__main__":
    lst = range(10)

    print(binary_search(lst, 12))
    print(binary_search(lst, 6))
