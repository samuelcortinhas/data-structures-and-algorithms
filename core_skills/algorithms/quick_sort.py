class QuickSort:
    # Time O(n^2) worst case but O(n log n) on average. Memory O(1)
    def __init__(self, array):
        self.array = array

    def quick_sort(self, left, right):
        if right - left < 1:
            return

        pivot = right
        swap_count = 0
        for i, x in enumerate(self.array[left : right + 1]):
            if x <= self.array[pivot]:
                tmp = self.array[left + swap_count]
                self.array[left + swap_count] = x
                self.array[left + i] = tmp
                swap_count += 1

        self.quick_sort(left, left + swap_count - 2)
        self.quick_sort(left + swap_count, right)

    def __call__(self):
        self.quick_sort(0, len(self.array) - 1)
        return self.array


print(QuickSort([4, 5, 6, 1, 7, 3])())
