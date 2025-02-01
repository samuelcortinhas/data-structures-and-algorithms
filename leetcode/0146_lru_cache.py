class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Memory O(n)
        self.capacity = capacity
        self.cache = {}  # Pair: (key, Node)
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert_right(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        # Time O(1) on average
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_right(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # Time O(1) on average
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert_right(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
