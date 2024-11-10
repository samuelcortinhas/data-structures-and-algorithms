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


if __name__ == "__main__":
    print(Node(5))
