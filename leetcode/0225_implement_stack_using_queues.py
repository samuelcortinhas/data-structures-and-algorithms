from collections import deque


class MyStack:
    # Single queue solution
    def __init__(self):
        # Memory O(n)
        self.queue = deque()
        self.count = 0

    def push(self, x: int) -> None:
        # Time O(1)
        self.queue.append(x)
        self.count += 1

    def pop(self) -> int:
        # Time O(n)
        for _ in range(self.count - 1):
            self.queue.append(self.queue.popleft())
        self.count -= 1
        return self.queue.popleft()

    def top(self) -> int:
        # Time O(1)
        return self.queue[-1]

    def empty(self) -> bool:
        # Time O(1)
        return self.count == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
