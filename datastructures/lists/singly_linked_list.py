class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def is_empty(self):
        return not self.count

    def add_first(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            temp = self.head
            node.next = temp
            self.head = node
        self.count += 1

    def add_last(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.count += 1

    def remove_first(self):
        if self.is_empty():
            return
        self.head = self.head.next
        self.count -= 1

        if self.count <= 1:
            self.head = self.tail

    def remove_last(self):
        if self.is_empty():
            return
        if self.count == 1:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.count -= 1
        if self.count == 1:
            self.head = self.tail

    def remove(self, value):
        if self.is_empty():
            return
        previous = None
        current = self.head
        while current is not None:
            if current.value == value:
                if self.count == 1:
                    self.head = self.tail = None
                    break
                if previous is None:
                    self.head = self.head.next
                else:
                    previous.next = current.next
                    if previous.next is None:
                        self.tail = previous
                self.count -= 1
            previous = current
            current = current.next

    def enumerate(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
