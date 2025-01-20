from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Tortoise and Hare
        # Time O(n), Memory O(1)
        if not head:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

    # def hasCycleTryExcept(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     # Floyd's Tortoise and Hare
    #     # Time O(n), Memory O(1)
    #     try:
    #         slow = head
    #         fast = head.next
    #         while slow is not fast:
    #             slow = slow.next
    #             fast = fast.next.next
    #         return True
    #     except:
    #         return False

    # def hasCycleHistory(self, head):
    #     # Time O(n^2), Memory O(n)
    #     history = []
    #     current = head
    #     while current:
    #         if current in history:
    #             return True
    #         history.append(current)
    #         current = current.next

    #     return False

    # def hasCycleHacky(self, head):
    #     # Hacky solution because of constraint len list < 10^4
    #     current = head
    #     i = 0
    #     while current:
    #         current = current.next
    #         i += 1
    #         if i > 10**4:
    #             return True
    #     return False

    # def hasCycleTwoPointer(self, head):
    #     # idea: cycle occurs if a node has 2 nodes pointing to it (except at head)
    #     current = head
    #     if not head:
    #         return False

    #     prev = None

    #     while current:
    #         try:
    #             if current.prev:
    #                 return True
    #         except:
    #             pass

    #         current.prev = prev

    #         next = current.next
    #         if not next:
    #             return False

    #         prev = current
    #         current = next
