import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Use priority queue/ min heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time O(n log k), Memory O(k) where n = total number of nodes
        h = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))  # i there to break ties

        curr = ListNode()
        head = curr
        while h:
            node = heapq.heappop(h)  # pop smallest node
            curr.next = node[2]
            nxt = node[2].next
            if nxt:
                heapq.heappush(h, (nxt.val, node[1], nxt))  # push next node
            curr = curr.next
        return head.next


# class Solution:
#     # Divide and conquer - merge 2 lists at a time
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # Time O(n log k), Memory O(k) where n = total number of nodes
#         if not lists:
#             return None

#         while len(lists) > 1:
#             merged_lists = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if i + 1 < len(lists) else None
#                 merged_lists.append(self.mergeTwoLists(l1, l2))
#             lists = merged_lists
#         return lists[0]

#     def mergeTwoLists(self, l1, l2):
#         # Time O(n), Memory O(1)
#         if not l1:
#             return l2
#         if not l2:
#             return l1

#         curr = ListNode()
#         head = curr
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         if l1:
#             curr.next = l1
#         if l2:
#             curr.next = l2
#         return head.next
