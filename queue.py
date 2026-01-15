class Queue:
    """
    Queue data structure implementation.
    FIFO principle: First In, First Out
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the front item of the queue."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Returns the front item without removing it."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())

    print("Dequeued:", queue.dequeue())
    print("Front element after dequeue:", queue.peek())
