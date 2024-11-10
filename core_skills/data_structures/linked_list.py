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

    linked_list = []

    def __init__(self, lst):
        lst.reverse()
        for x in lst:
            node = Node(x)
            if self.linked_list:
                node.self_node = self.linked_list[-1]
            self.linked_list.append(node)
        self.linked_list.reverse()

    def __repr__(self):
        return "<Linked list: {}>".format(self.linked_list)


if __name__ == "__main__":
    print(Node(5))
    print(LinkedList([1, 2, 3]))
