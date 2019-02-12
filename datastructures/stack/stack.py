from datastructures.lists.singly_linked_list import LinkedList
from datastructures.lists.node import SingleLinkedNode


class StackList:
    def __init__(self):
        self._items = LinkedList()

    def push(self, item):
        self._items.add_first(SingleLinkedNode(item))

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty!")

        top_element = self._items.head.value
        self._items.remove_first()
        return top_element

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty!")

        return self._items.head.value

    def is_empty(self):
        return self._items.count == 0

    def size(self):
        return self._items.count


class StackArray:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self.size() == 0

    def push(self, i):
        self._items.append(i)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty!")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty!")

        return self._items[-1]

    def size(self):
        return len(self._items)
