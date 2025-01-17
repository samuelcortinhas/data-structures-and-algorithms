from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time O(n), Memory O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get size of list
        curr = head
        sz = 0
        while curr:
            sz += 1
            curr = curr.next

        # base case
        curr = head
        if sz == n:
            return head.next

        # go to previous node of node being removed
        steps = sz - n - 1
        for _ in range(steps):
            curr = curr.next

        # remove node
        curr.next = curr.next.next

        return head
