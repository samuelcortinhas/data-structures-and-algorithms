from collections import defaultdict


class TimeMap:
    def __init__(self):
        # Memory O(n)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time O(1)
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Time O(log n)
        entry = self.store[key]
        left = 0
        right = len(entry) - 1
        while left < right:
            mid = (left + right) // 2
            if entry[mid][1] == timestamp:
                return entry[mid][0]
            elif entry[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if left < len(entry) and entry[left][1] <= timestamp:
            return entry[left][0]
        elif left > 0 and entry[left - 1][1] <= timestamp:
            return entry[left - 1][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
