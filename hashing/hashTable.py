class HashMap:
    def __init__(self, size):
        self._size = self._get_prime_number(size)
        self._keys = [None] * self._size
        self._values = [None] * self._size

    @staticmethod
    def _get_prime_number(size):
        for num in range(size * 2, size * 3):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                return num

    def hashit(self, key):
        return key % self._size

    def rehashit(self, hashed_idx):
        return (hashed_idx + 1) % self._size

    def put(self, key, value):
        hashed_key = self.hashit(key)
        if self._keys[hashed_key] is None:
            self._keys[hashed_key] = key
            self._values[hashed_key] = value
        elif self._keys[hashed_key] == key:
                self._values[hashed_key] = value
        else:
            nextslot = self.rehashit(hashed_key)
            while (self._keys[nextslot] is not None and
                   self._keys[nextslot] != key):
                nextslot = self.rehashit(hashed_key)
            if self._keys[nextslot] is None:
                self._keys[nextslot] = key
                self._values[nextslot] = value
            else:
                self._values[nextslot] = value

    def get(self, key):
        startslot = self.hashit(key)
        value = None
        stop = False
        found = False
        idx = startslot
        while self._keys[idx] is not None and not found and not stop:
            if self._keys[idx] == key:
                found = True
                value = self._values[idx]
            else:
                idx = self.rehashit(idx)
                if idx == startslot:
                    stop = True
        return value

    def __getitem__(self, value):
        return self.get(value)

    def __setitem__(self, key, value):
        self.put(key, value)
