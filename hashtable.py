""" HashTable Practice Implementation """

class HashTable:
    """A custom implementation of a HashTable in Python"""

    def __init__(self, size=2**20):
        self.size = size
        self.array = [None] * self.size

    def __iter__(self):
        return iter(self.array)

    def __len__(self):
        return self.size

    def set(self, key: object, value: object) -> None:
        """Saves an object in the HashTable. The passed object must be hashable."""
        hash_key = hash(key) % self.size
        curr_val = self.array[hash_key]
        if curr_val is None:
            self.array[hash_key] = value
            return

        raise KeyError('Hash collision')

    def get(self, key: object) -> object:
        """Return the object identified by key, or None if the key is not valid."""
        return self.array[(hash(key) % len(self.array))]
