class RecursiveBinarySearch:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def recursive_binary_search(self, start, end):
        """
        Assumes list is sorted.
        O(log(n)) time complexity
        O(1) space complexity
        """
        if start > end:
            return

        midpoint = (start + end) // 2

        if self.lst[midpoint] == self.target:
            return midpoint
        elif self.lst[midpoint] < self.target:
            return self.recursive_binary_search(midpoint + 1, end)
        else:
            return self.recursive_binary_search(start, midpoint - 1)

    def __call__(self):
        return self.recursive_binary_search(0, len(self.lst) - 1)


if __name__ == "__main__":
    lst = range(10)

    print(RecursiveBinarySearch(lst, 12)())
    print(RecursiveBinarySearch(lst, 6)())
