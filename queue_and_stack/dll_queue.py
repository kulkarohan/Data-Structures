import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.storage.length > 0:
            removed_node_value = self.storage.head.value
            self.storage.remove_from_head()
            self.size -= 1

            return removed_node_value

    def len(self):
        return self.size
