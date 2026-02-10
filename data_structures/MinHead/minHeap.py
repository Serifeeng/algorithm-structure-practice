class MinHeap:
    """
    Min Heap (Priority Queue) implementation.
    """

    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Inserts a value into the heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def remove_min(self):
        """Removes and returns the minimum element."""
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        """Returns the minimum element without removing it."""
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)

    print("Min element:", heap.peek())
    print("Removed:", heap.remove_min())
    print("Min element after removal:", heap.peek())
