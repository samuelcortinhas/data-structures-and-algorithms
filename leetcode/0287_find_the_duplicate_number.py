from typing import List

"""
Explanation. 
nums gives rise to a linked list with a cycle starting at the duplicate number.
We use Floyd's slow and fast algorithm to identify the cycle. 
But where slow=fast isn't actually the duplicate number.

Let p be the number of steps from 0 to duplicate number. (i.e. #previous steps)
Let x be the number of steps from where slow=fast to the duplicate number.
Let c by the length of the cycle. 

The slow pointer travels p + c-x steps. 
The fast pointer travels p + kc + c-x, where k is an unknown integer. 
We also know that fast = 2*slow, therefore we have

2(p+c-x) = p+kc+c-x
2p+2c-2x = p+kc+c-x
p+c = kc+x
p = x + (k-1)c

And since the first slow pointer is inside the cycle, taking mod c we get p=x.
That means we can use a second slow2 pointer and iterate until slow=slow2,
ensuring that we arrive at the duplicate number.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time O(n), Memory O(1)
        # Floyd's cycle detection
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

    # def findDuplicateWithSet(self, nums: List[int]) -> int:
    #     # Time O(n), Memory O(n)
    #     seen = set()
    #     for n in nums:
    #         if n in seen:
    #             return n
    #         seen.add(n)
