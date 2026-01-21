class HashTable:
    """
    Simple Hash Table implementation using separate chaining.
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Generates a hash value for a given key."""
        return hash(key) % self.size

    def put(self, key, value):
        """Inserts or updates a key-value pair."""
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):
        """Retrieves the value associated with a key."""
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        """Removes a key-value pair from the hash table."""
        index = self._hash(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return

    def display(self):
        """Displays the contents of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
    ht = HashTable()

    ht.put("name", "Serife")
    ht.put("age", 22)
    ht.put("city", "Istanbul")

    print("Name:", ht.get("name"))
    print("Age:", ht.get("age"))

    ht.remove("age")
    ht.display()
