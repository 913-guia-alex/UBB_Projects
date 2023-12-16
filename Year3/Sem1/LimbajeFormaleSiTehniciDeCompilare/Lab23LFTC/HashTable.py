from typing import Any, Tuple


# 1a
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.items = [[] for _ in range(size)]

    def _hash(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        raise TypeError(f"Unsupported key type: {type(key)}")

    def add(self, key: Any) -> Tuple[int, int]:
        hash_value = self._hash(key)
        if key not in self.items[hash_value]:
            self.items[hash_value].append(key)
            return hash_value, self.items[hash_value].index(key)
        return hash_value, self.items[hash_value].index(key)

    def contains(self, key: Any) -> bool:
        hash_value = self._hash(key)
        return key in self.items[hash_value]

    def get_position(self, key: Any) -> Tuple[int, int]:
        hash_value = self._hash(key)
        if key in self.items[hash_value]:
            return hash_value, self.items[hash_value].index(key)
        return -1, -1

    def __str__(self):
        return f"HashTable{{items={self.items}}}"
