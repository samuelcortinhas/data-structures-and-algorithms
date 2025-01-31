from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Time O(n), Memory O(n)
        if not head:
            return None

        curr = head
        copy_head = Node(head.val)
        copy_curr = copy_head
        old_to_new = {head: copy_head}
        while curr:
            nxt = curr.next
            rndm = curr.random

            if nxt in old_to_new:
                copy_nxt = old_to_new[nxt]
            else:
                copy_nxt = Node(nxt.val) if nxt else None
                old_to_new[nxt] = copy_nxt

            if rndm in old_to_new:
                copy_rndm = old_to_new[rndm]
            else:
                copy_rndm = Node(rndm.val) if rndm else None
                old_to_new[rndm] = copy_rndm

            copy_curr.next = copy_nxt
            copy_curr.random = copy_rndm

            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head
