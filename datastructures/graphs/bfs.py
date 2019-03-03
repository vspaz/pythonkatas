class Deque:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def extend(self, items):
        self._items.extend(items)

    def __add__(self, items):
        self._items.extend(items)
        return self


graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


def search(name):
    search_dequeue = Deque()
    search_dequeue += graph[name]
    searched = set()
    while not search_dequeue.is_empty():
        person = search_dequeue.remove_rear()
        if person not in searched:
            if person == "jonny":
                print("found")
                return True
            else:
                search_dequeue += graph[person]
                searched.add(person)


if __name__ == "__main__":
    search("you")
