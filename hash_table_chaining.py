class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_key]):
            k, v = kv
            if key == k:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self.hash_function(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_key = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_key]):
            k, v = kv
            if k == key:
                del self.table[hash_key][i]
                return True
        return False
