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
            if v == 0 or x == x_ref or y == y_ref or abs(y - y_ref) != abs(x - x_ref):
                continue
            corner1, corner2 = (x_ref, y), (x, y_ref)
            res += self.points[corner1] * self.points[corner2] * v
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
