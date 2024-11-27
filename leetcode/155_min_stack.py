class MinStack(object):
    """
    Time O(1), Memory O(n) for all methods
    """

    def __init__(self):
        self.stack = []
        self.mins = [float("inf")]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
