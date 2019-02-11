
class SingleLinkedNode:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class DoubleLinkedNode(SingleLinkedNode):
    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self.prev = prev
