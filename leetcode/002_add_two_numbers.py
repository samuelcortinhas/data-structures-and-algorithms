# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Time O(n), Memory O(n) where n is max length of two linked lists
        head = current = ListNode(0)
        rem = 0

        while l1 or l2 or rem:
            v = rem
            if l1:
                v += l1.val
                l1 = l1.next

            if l2:
                v += l2.val
                l2 = l2.next

            if v >= 10:
                current.next = ListNode(v - 10)
                rem = 1
            else:
                current.next = ListNode(v)
                rem = 0

            current = current.next

        return head.next
