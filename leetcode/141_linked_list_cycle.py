# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Time O(n^2), Memory O(n)
        history = []
        current = head
        while current:
            if current in history:
                return True
            history.append(current)
            current = current.next

        return False
