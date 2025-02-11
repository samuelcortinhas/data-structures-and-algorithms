class Solution:
    @staticmethod
    def nextStep(n):
        return sum([int(d) ** 2 for d in str(n)])

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.nextStep(n)
        while slow != fast:
            slow = self.nextStep(slow)
            fast = self.nextStep(self.nextStep(fast))
        return fast == 1
