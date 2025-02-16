from typing import List


class Solution:
    def minMeetingRoomsV2(self, intervals: List[List[int]]) -> int:
        # Time O(2n log n), Memory O(n)
        start = [None] * len(intervals)
        end = [None] * len(intervals)
        for i, (a, b) in enumerate(intervals):
            start[i] = a
            end[i] = b

        start.sort()
        end.sort()
        i, j = 0, 0
        count, max_count = 0, 0
        while i < len(intervals) and j < len(intervals):
            if start[i] < end[j]:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1

        while i < len(intervals):
            count += 1
            max_count = max(max_count, count)
            i += 1

        return max_count

    # def minMeetingRoomsV1(self, intervals: List[List[int]]) -> int:
    #     # Time O(2n log 2n), Memory O(n)
    #     times = []
    #     for start, end in intervals:
    #         times.append((start, "start"))
    #         times.append((end, "end"))

    #     times.sort()
    #     curr_rooms, max_rooms = 0, 0
    #     for t, a in times:
    #         if a == "start":
    #             curr_rooms += 1
    #             max_rooms = max(max_rooms, curr_rooms)
    #         elif a == "end":
    #             curr_rooms -= 1
    #     return max_rooms
