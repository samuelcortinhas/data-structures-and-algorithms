class Node:
    """
    A single node of a linked list.
    Each node stores some data and a reference to the next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "<Node data: {}>".format(self.data)


class LinkedList:
    """
    A singly linked list made up of nodes.
    Each node stores some data and a reference to the next node in the list.
    """

    def __init__(self):
        self.head = None

    def _is_empty(self):
        return self.head == None

    def __len__(self):
        if self._is_empty():
            return 0

        i = 1
        current = self.head
        while current.next_node:
            i += 1
            current = current.next_node

        return i

    def add(self, value):
        """
        Add node with value to head of linked list.
        O(1) time complexity.
        """
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def search(self, value):
        """
        Search for value in linked list.
        Return true if found otherwise false.
        """
        if self._is_empty():
            return False

        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next_node

        return False


if __name__ == "__main__":
    print(Node(5))
