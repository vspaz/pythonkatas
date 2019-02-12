class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def is_empty(self):
        return not self.count

    def add_first(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp
        if self.count == 0:
            self.tail = self.head
        else:
            temp.prev = self.head
        self.count += 1

    def add_last(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def remove_first(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1

        if self.count <= 1:
            self.head = self.tail

    def remove_last(self):
        if self.is_empty():
            return
        if self.count == 1:
            self.head = self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        self.count -= 1
        if self.count == 1:
            self.head = self.tail

    def remove(self, value):
        if self.is_empty():
            return
        current = self.head
        while current is not None:
            if current.value == value:
                if self.count == 1:
                    self.head = self.tail = None
                    break
                if current.prev is None:
                    self.head = self.head.next
                else:
                    current.prev.next = current.next
                    if current.prev.next is None:
                        self.tail = current.prev
                self.count -= 1
            current = current.next

    def enumerate(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def contains(self, target):
        for value in self.enumerate():
            if value is None:
                return False
            if value == target:
                return True
