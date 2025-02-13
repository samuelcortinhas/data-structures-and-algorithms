from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        # Memory O(n)
        self.points = defaultdict(int)  # point: count

    def add(self, point: List[int]) -> None:
        # Time O(1)
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # Time O(n)
        x_ref, y_ref = point[0], point[1]
        res = 0
        for (x, y), v in list(self.points.items()):
            if v == 0 or x == x_ref or y == y_ref:
                continue

            m = (y - y_ref) / (x - x_ref)
            if m == 1:
                corner1 = (min(x, point[0]), max(y, point[1]))
                corner2 = (max(x, point[0]), min(y, point[1]))
            elif m == -1:
                corner1 = (max(x, point[0]), max(y, point[1]))
                corner2 = (min(x, point[0]), min(y, point[1]))
            else:
                continue

            res += self.points[corner1] * self.points[corner2] * v
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
