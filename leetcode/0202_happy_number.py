class Solution:
    @staticmethod
    def nextStep(n):
        res = 0
        for digit in list(str(n)):
            res += int(digit) ** 2
        return res

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.nextStep(n)
        while slow != fast and fast != 1:
            slow = self.nextStep(slow)
            fast = self.nextStep(self.nextStep(fast))
        return fast == 1
