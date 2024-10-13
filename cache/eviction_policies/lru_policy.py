

from data_structures.doubly_linked_list import DoublyLinkedList, Node
from eviction_policies.abstract_eviction_policy import AbstractEvictionPolicy


class LRUPolicy(AbstractEvictionPolicy):
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.mapping = {}

    def update(self, key):
        if key in self.mapping:
            node = self.mapping[key]
            self.dll.remove(node)
            self.dll.add_to_front(node)
        else:
            node = Node(key)
            self.mapping[key] = node
            self.dll.add_to_front(node)

    def evict(self):
        if self.dll.tail.prev != self.dll.head:
            removed_node = self.dll.remove_from_end()
            del self.mapping[removed_node.key]
            return removed_node.key
        return None