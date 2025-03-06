from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Time O(n^2), Memory O(1)
        n_squared = len(grid) * len(grid)
        expected_sum = n_squared * (n_squared + 1) // 2
        expected_sum_of_squares = n_squared * (n_squared + 1) * (2 * n_squared + 1) // 6

        actual_sum = 0
        actual_sum_of_squares = 0
        for row in grid:
            for v in row:
                actual_sum += v
                actual_sum_of_squares += v * v

        # a - b
        diff_sum = actual_sum - expected_sum

        # a² - b²
        diff_sum_of_squares = actual_sum_of_squares - expected_sum_of_squares

        # a + b = (a² - b²) / (a - b)
        sum_a_b = diff_sum_of_squares // diff_sum

        # Now we can find a and b
        a = (sum_a_b + diff_sum) // 2
        b = (sum_a_b - diff_sum) // 2

        return [a, b]

    # def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    #     # Time O(n^2), Memory O(n^2)
    #     n = len(grid)
    #     seen = set()
    #     a, b = None, None
    #     for row in grid:
    #         for v in row:
    #             if v in seen:
    #                 a = v
    #             seen.add(v)

    #     (b,) = set(range(1, 1 + n * n)).difference(seen)
    #     return [a, b]
