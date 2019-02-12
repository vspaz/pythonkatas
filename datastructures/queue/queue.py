from datastructures.lists.singly_linked_list import LinkedList
from datastructures.lists.node import SingleLinkedNode


class QueueList:
    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        return 0 == self._items.count

    def enqueue(self, item):
        self._items.add_last(SingleLinkedNode(item))

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty!")
        first = self._items.head.value
        self._items.remove_first()
        return first

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty!")
        return self._items.head.value

    def size(self):
        return self._items.count


class QueueArray:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return 0 == self._items

    def size(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty!")
        return self._items.pop(0)

    def peek(self):
        return self._items[0]
