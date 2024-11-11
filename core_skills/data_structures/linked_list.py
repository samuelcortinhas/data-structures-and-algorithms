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
        """
        Returns number of nodes in linked list.
        O(n) time complexity.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node

        return count

    def insert_head(self, value):
        """
        Add node with value to the head of linked list.
        O(1) time complexity.
        """
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def insert_tail(self, value):
        """
        Add node with value to the tail of linked list.
        O(n) time complexity.
        """
        current = self.head
        if not current:
            self.insert_head(value)
            return

        while current.next_node:
            current = current.next_node

        current.next_node = Node(value)

    def search(self, value):
        """
        Search for node with value in linked list.
        O(n) time complexity.
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node

    def insert(self, value, index):
        """
        Insert node with value into linked list at specified index.
        O(n) time complexity.
        """
        if index > self.__len__:
            return

        if index == 0:
            self.insert_head(value)
            return

        current = self.head

        i = 0
        while i < index - 1:
            if not current:
                return
            i += 1
            current = current.next_node

        node = Node(value)
        if current.next_node:
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

    def __repr__(self):
        """
        String representation of linked list.
        O(n) time complexity.
        """
        values = self.get_values()
        return "Linked list: " + " -> ".join([str(v) for v in values])


if __name__ == "__main__":
    print(Node(5))
    L = LinkedList()
    L.insert_head(1)
    L.insert_head(2)
    L.insert_head(3)
    L.insert(value=10, index=2)
    print(L)
