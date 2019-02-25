
class Iterator:
    def __iter__(self):
        return self

    def __init__(self, num):
        self.num = num
        self.count = 0

    def __next__(self):
        if self.count < self.num:
            self.count += 1
            return self.count
        else:
            raise StopIteration


if __name__ == "__main__":
    iterator = Iterator(10)
    assert 1 == next(iterator)
    assert 2 == next(iterator)
