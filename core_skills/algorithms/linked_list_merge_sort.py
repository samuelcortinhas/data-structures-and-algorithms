import sys

sys.path.insert(0, "./core_skills")

from data_structures.linked_list import LinkedList

l = LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)

print(l)
