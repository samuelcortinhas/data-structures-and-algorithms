from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Time O(n), Memory O(1)
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        right = slow
        left = prev
        res = 0
        while right:
            res = max(res, right.val + left.val)
            right = right.next
            left = left.next
        return res

    # def pairSumDouble(self, head: Optional[ListNode]) -> int:
    #     # Time O(n), Memory O(n)
    #     prev = None
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         slow.prev = prev
    #         prev = slow
    #         slow = slow.next
    #         fast = fast.next.next

    #     right = slow
    #     left = prev
    #     res = 0
    #     while right:
    #         res = max(res, right.val + left.val)
    #         right = right.next
    #         left = left.prev
    #     return res
