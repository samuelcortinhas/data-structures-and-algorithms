from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time O(n), Memory O(n/k)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        # reverse the group
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # now `head` is the tail of the current group
        # and `curr` is the head of the next group
        head.next = self.reverseKGroup(curr, k)
        return prev
