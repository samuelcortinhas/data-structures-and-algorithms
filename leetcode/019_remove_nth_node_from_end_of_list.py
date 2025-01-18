from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time O(n), Memory O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy list of length n
        dummy = ListNode()
        lag = dummy
        for _ in range(n - 1):
            dummy.next = ListNode()
            dummy = dummy.next

        # join dummy list to list
        dummy.next = head

        # iterate until end, then lag is (n+1)th from end
        curr = head
        sz = 1
        while curr.next:
            sz += 1
            curr = curr.next
            lag = lag.next

        # remove n-th node from end
        lag.next = lag.next.next

        # edge case if removing head
        if n == sz:
            return head.next

        # return head
        return head

    # def removeNthFromEndTwoPasses(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     # get size of list
    #     curr = head
    #     sz = 0
    #     while curr:
    #         sz += 1
    #         curr = curr.next

    #     # base case
    #     curr = head
    #     if sz == n:
    #         return head.next

    #     # go to previous node of node being removed
    #     steps = sz - n - 1
    #     for _ in range(steps):
    #         curr = curr.next

    #     # remove node
    #     curr.next = curr.next.next

    #     return head
