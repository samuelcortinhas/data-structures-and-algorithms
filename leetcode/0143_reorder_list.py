from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time O(n), Memory O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # find middle
        mid_index = (length - 1) // 2
        curr = head
        for _ in range(mid_index):
            curr = curr.next
        mid = curr

        # break connection between 2 halves
        right = mid.next
        mid.next = None

        # reverse right half
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt

        # alternating merge
        curr = head
        L = head.next
        R = prev

        k = 1
        while k < length:
            if (k % 2) == 0:
                curr.next = L
                L = L.next
            else:
                curr.next = R
                R = R.next

            curr = curr.next
            k += 1
