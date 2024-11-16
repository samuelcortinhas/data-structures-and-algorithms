class MergeSort:
    """
    Sorts an array in ascending order.

    1. Divide -> split array into 2 halves.
    2. Conquer -> sort each half recursively.
    3. Combine -> merge sorted halves together.

    O(n log n) time complexity.
    O(n) space complexity.
    """

    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        left, right = self.split_array(arr)
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)

        return self.merge(left_sorted, right_sorted)

    @staticmethod
    def split_array(arr):
        mid = len(arr) // 2
        return arr[mid:], arr[:mid]

    @staticmethod
    def merge(left_sorted, right_sorted):
        """
        Merges two arrays, sorting them in the process.
        """
        l = []
        i, j = 0, 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                l.append(left_sorted[i])
                i += 1
            else:
                l.append(right_sorted[j])
                j += 1

        l += left_sorted[i:] + right_sorted[j:]

        return l

    def __call__(self):
        return self.merge_sort(self.arr)


def verify_sorted(arr):
    if len(arr) <= 1:
        return True

    return arr[0] <= arr[1] and verify_sorted(arr[1:])


if __name__ == "__main__":
    array = [18, 18, 13, 7, 20, 6, 6, 1, 10, 3]

    print("array:", array)
    print("sorted:", verify_sorted(array))

    sorted_array = MergeSort(array)()

    print("\narray:", sorted_array)
    print("sorted:", verify_sorted(sorted_array))
