class Node:
    # Doubly linked list node
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.nxt = nxt


class Deque:
    # Doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if (self.head is None) or (self.tail is None):
            return True
        return False

    def append(self, value: int) -> None:
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node

    def appendleft(self, value: int) -> None:
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head.prev = node
            self.head = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        tail = self.tail
        prev = tail.prev
        self.tail = prev

        if self.tail:
            self.tail.nxt = None
        else:
            self.head = None

        return tail.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        head = self.head
        nxt = head.nxt
        self.head = nxt

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return head.value
