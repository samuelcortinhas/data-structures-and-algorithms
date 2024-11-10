class Node:
    """
    A single node of a linked list.
    Each node stores some data and a reference to the next node in the list.
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: {}>".format(self.data)


if __name__ == "__main__":
    print(Node(5))
