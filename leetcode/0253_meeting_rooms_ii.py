from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time O(n log n), Memory O(n)
        times = []
        for start, end in intervals:
            times.append((start, "start"))
            times.append((end, "end"))

        times.sort()
        curr_rooms, max_rooms = 0, 0
        for t, a in times:
            if a == "start":
                curr_rooms += 1
                max_rooms = max(max_rooms, curr_rooms)
            elif a == "end":
                curr_rooms -= 1
        return max_rooms
