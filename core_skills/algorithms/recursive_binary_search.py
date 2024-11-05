def recursive_binary_search(lst, target):
    """
    Assumes list is sorted.
    O(log(n)) time complexity
    """
    if len(lst) == 0:
        return False

    midpoint = (len(lst) - 1) // 2

    if lst[midpoint] == target:
        return True
    elif lst[midpoint] < target:
        return recursive_binary_search(lst[midpoint + 1 :], target)
    else:
        return recursive_binary_search(lst[:midpoint], target)


if __name__ == "__main__":
    lst = range(10)

    print(recursive_binary_search(lst, 12))
    print(recursive_binary_search(lst, 6))
