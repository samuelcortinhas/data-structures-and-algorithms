import sys

sys.path.insert(0, "./core_skills")

from data_structures.linked_list import LinkedList


class MergeSortLinkedList:
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def merge_sort(self, linked_list):
        """
        Sorts a linked list in ascending order.

        1. Divide -> bisect linked list into 2 linked lists.
        2. Conquer -> sort each half recursively.
        3. Combine -> merge each half back into a single sorted linked list.

        O(n log n) time complexity.
        O(n) space complexity.
        """

        if linked_list.__len__() <= 1:
            return linked_list

        left, right = self.split(linked_list)
        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)

        return self.merge(left_sorted, right_sorted)

    @staticmethod
    def split(linked_list):
        """
        Splits linked list into 2 halves.
        Returns two linked lists.
        """

        mid = linked_list.__len__() // 2
        mid_node = linked_list.get_at_index(mid - 1)

        left_list = linked_list
        right_list = LinkedList()
        right_list.head = mid_node.next_node
        mid_node.next_node = None

        return left_list, right_list

    @staticmethod
    def merge(left_sorted, right_sorted):
        """
        Merges two sorted linked lists into one sorted linked list.
        """
        left_head = left_sorted.head
        right_head = right_sorted.head
        l = LinkedList()
        l.insert_head(0)  # add fake head
        current = l.head

        while left_head and right_head:
            if left_head.data <= right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

            current = current.next_node

        if left_head:
            current.next_node = left_head
        elif right_head:
            current.next_node = right_head

        l.head = l.head.next_node  # remove fake head

        return l

    def __call__(self):
        return self.merge_sort(self.linked_list)


def verify_sorted(linked_list):
    if linked_list.__len__() <= 1:
        return True

    current = linked_list.head
    next = current.next_node
    L = LinkedList()
    L.head = next

    return (current.data <= next.data) and verify_sorted(L)


if __name__ == "__main__":
    l = LinkedList()
    l.insert_head(81)
    l.insert_head(98)
    l.insert_head(69)
    l.insert_head(81)
    l.insert_head(67)
    l.insert_head(4)
    l.insert_head(17)

    print(l)
    print(verify_sorted(l))

    sorted_linked_list = MergeSortLinkedList(l)()
    print(sorted_linked_list)
    print(verify_sorted(sorted_linked_list))
