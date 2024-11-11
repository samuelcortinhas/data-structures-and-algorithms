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
        O(n) time complexity.
        """
        if self._is_empty():
            return False

        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next_node

        return False

    def insert(self, value, index):
        """
        Insert node with value into linked list at specified index.
        O(n) time complexity.
        """
        if index == 0:
            self.add(value)
            return

        current = self.head
        new_node = Node(value)

        i = 0
        current = self.head
        while (i < index) and current:
            i += 1
            current = current.next_node

        node = Node(value)
        node.next_node = current.next_node.next_node
        current.next_node = node

    def node_at_index(self, index):
        """
        Returns value of node at index.
        O(n) time complexity.
        """
        if self._is_empty():
            return

        i = 0
        current = self.head
        while i < index:
            if not current:
                return

            i += 1
            current = current.next_node

        if current:
            return current.data

    def get_values(self):
        """
        Returns an array of all the values in order.
        O(n) time complexity.
        """
        if self._is_empty():
            return []

        values = []
        current = self.head
        while current.next_node:
            values.append(current.data)
            current = current.next_node

        values.append(current.data)

        return values


if __name__ == "__main__":
    print(Node(5))
