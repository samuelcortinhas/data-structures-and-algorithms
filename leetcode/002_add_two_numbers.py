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
        a1 = []
        a2 = []

        while l1:
            a1.append(l1.val)
            l1 = l1.next

        while l2:
            a2.append(l2.val)
            l2 = l2.next

        i = len(a1)
        j = len(a2)

        out = []

        if i > j:
            a2 = a2 + [0] * (i - j)
        elif j > i:
            a1 = a1 + [0] * (j - i)

        rem = 0
        for x, y in zip(a1, a2):
            if x + y + rem >= 10:
                out.append(x + y - 10 + rem)
                rem = 1
            else:
                out.append(x + y + rem)
                rem = 0

        if rem == 1:
            out.append(1)

        head = ListNode(out[0])
        current = head

        for u in out[1:]:
            current.next = ListNode(u)
            current = current.next

        return head
